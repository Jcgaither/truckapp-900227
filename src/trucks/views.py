from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.utils.functional import cached_property
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.template import RequestContext, Context
from django.template.loader import get_template
from actstream.models import followers, Action
from trucks.forms import BaseTruckCreateForm, BaseDeleteRequest, PlusTruckCreateForm, PlusTruckUpdateForm, EmailCollectionForm, EventCreateForm, FeedbackForm
from trucks.models import BaseTruck, PlusTruck, EmailCollection, Event, Feedback
from profiles.models import Profile
from permission.decorators import permission_required
from actstream.models import actor_stream, Follow
from actstream import action


class MultipleObjectMixin(object):
	def get_object(self, queryset=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		if slug:
			try:
				obj = self.model.objects.get(slug=slug)
			except self.model.MultipleObjectsReturned:
				obj = self.get_queryset().first()
			except:
				raise Http404
			return obj
		return Http404



""" BaseTruck create view """

class TruckCreateView(CreateView):
	form_class = BaseTruckCreateForm
	template_name = 'trucks/add_truck.html'

	def form_valid(self,form):
		form.instance.added_by = self.request.user
		return super(TruckCreateView, self).form_valid(form)

	def get_success_url(self):
		messages.success(self.request, "BaseTruck successfully added!")
		return reverse("home")


""" Delete Request view """

class TruckDeleteView(FormView):
	form_class = BaseDeleteRequest
	template_name = 'trucks/truck_delete.html'

	def form_valid(self,form):
		DeleteRequest = form.save(commit=False)
		DeleteRequest.user = self.request.user
		DeleteRequest.save()
		return super(TruckDeleteView, self).form_valid(form)


	def get_success_url(self):
		messages.success(self.request, "Request Sent")
		return reverse("home")

	def get_object(self, request):
		if request.user.is_authenticated():
			DeleteRequest.user = request.user
			DeleteRequest.user.save()
			DeleteRequest.truck = self.truck
			DeleteRequest.truck.save()
		return DeleteRequest.user, DeleteRequest.truck

""" Home Page view """

def TruckHomeView(request):
	recent_trucks = PlusTruck.objects.all().order_by('-id')[:6]
	if request.method == "POST":
		form = EmailCollectionForm(request.POST)
		if form.is_valid():
			contact_email = request.POST.get('email')
			template = get_template('trucks/mailinglist_template.txt')
			context = Context({
				'email': contact_email,
			})
			content = template.render(context)
			email = EmailMessage('Hey', content, "WheelDine <hello@wheeldine.com",
			[contact_email], reply_to=['hello@wheeldine.com']
			)
			email.send()
			EmailCollection = form.save(commit=False)
			EmailCollection.save()
			messages.success(request, "Successfully joined the mailing list!")
			return HttpResponseRedirect("")
	else:
		form = EmailCollectionForm()

	context = {"recent_trucks": recent_trucks, "form": form}
 	return render(request, 'trucks/home.html', context)

""" Form selection view """

def FormSelectView(request):
	return render(request, 'trucks/form_select.html')

""" Mapview """

class MapView(TemplateView):
	template_name  ='trucks/map.html'

	def get_context_data(self, **kwargs):
		context = super(MapView, self).get_context_data(**kwargs)
		context['popup'] = PlusTruck.objects.all()


""" PlusTruck CreateView """

class PlusTruckCreateView(SuccessMessageMixin, CreateView):
	form_class = PlusTruckCreateForm
	success_message = "PlusTruck: %(plus_truck_name)s was successfully created!"
	template_name = 'trucks/add_plus_truck.html'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.owner = self.request.user
		obj.save()
		return super(PlusTruckCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('home')




""" PlusTruck DeleteView """

@permission_required('trucks.delete_plustruck')
class PlusTruckDeleteView(DeleteView):
	model = PlusTruck
	template_name = 'trucks/plus_truck_delete.html'
	success_message = "Your PlusTruck was successfully deleted"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PlusTruckDeleteView, self).delete(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("home")

""" PlusTruck UpdateView """

@permission_required('trucks.change_plustruck')
class PlusTruckUpdateView(SuccessMessageMixin, UpdateView):
	model = PlusTruck
	form_class = PlusTruckUpdateForm
	success_message = "%(plus_truck_name)s was successfully updated"
	template_name = 'trucks/update.html'

	def form_valid(self, form):
		return super(PlusTruckUpdateView, self).form_valid(form)



""" PlusTruck Rank View """

def RankView(request):
	top_trucks = PlusTruck.objects.filter(top_truck=True)
	visitors = followers(PlusTruck)
	context = {'top_trucks': top_trucks, 'visitors': visitors}
	return render(request, 'trucks/truck_ranking.html', context)

""" PlusTruck Detail View """

class PlusTruckDetailView(DetailView):
	model = PlusTruck
	template_name = 'trucks/plus_truck_detail.html'

	def get_context_data(self, **kwargs):
		context = super(PlusTruckDetailView, self).get_context_data(**kwargs)
		context['visitors'] = followers(self.object)
		return context



	def get_object(self, queryset=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		if slug:
			try:
				obj = self.model.objects.get(slug=slug)
			except self.model.MultipleObjectsReturned:
				obj = self.get_queryset().first()
			except:
				raise Http404
			return obj


# """ PlusTruck Imageupload View """
#
# class PlusTruckImageUploadView(CreateView):
# 	form_class = PlusTruckImageForm
# 	template_name = 'trucks/add_image.html'
#
# 	def get_success_url(self):
# 		messages.success(self.request, "Images successfully uploaded")
# 		return self.food_truck.get_absolute_url()
#
# 	@cached_property
# 	def food_truck(self):
# 		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])
#
# 	def form_valid(self, form):
# 		file = form.save(commit=False)
# 		file.food_truck = self.food_truck
# 		file.save()
# 		return super(PlusTruckImageUploadView, self).form_valid(form)
#
# """ PlusTruck Image update View """
#
# class PlusTruckImageUpdateView(SuccessMessageMixin, UpdateView):
# 	model = PlusTruckImage
# 	fields = ['file',]
# 	success_message = "Images successfully updated"
# 	template_name = 'trucks/delete_image.html'
#
# 	def get_object(self):
# 		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])
#
# 	def form_valid(self, form):
# 		return super(PlusTruckImageUpdateView, self).form_valid(form)
#
#
# """ Image Detail View """
# class PlusTruckImageDetailView(DetailView):
# 	model = PlusTruckImage
# 	template_name = 'trucks/plus_truck_detail.html'
#
# 	def get_object(self):
# 		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])
#
# 	def get_context_data(self, **kwargs):
# 		context = super(PlusTruckImageDetailView, self).get_context_data(**kwargs)
# 		return context
# #
# """ Image Delete View """
# class PlusTruckImageDeleteView(DeleteView):
# 	model = PlusTruckImage
# 	template_name = 'trucks/delete_image.html'
# 	success_message = "Image successfully deleted"
#
# 	def get_object(self):
# 		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])
#
# 	def delete(self, request, *args, **kwargs):
# 		messages.success(self.request, self.success_message)
# 		return super(PlusTruckImageDeleteView, self).delete(request, *args, **kwargs)
#
# 	def get_success_url(self):
# 		return reverse('home')

""" Event Create View """

class EventCreateView(SuccessMessageMixin, CreateView):
	form_class = EventCreateForm
	success_message = "Event: %(event_name)s was successfully created"
	template_name = 'trucks/add_event.html'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.creator = self.request.user
		obj.save()
		return super(EventCreateView, self).form_valid(form)


	def get_success_url(self):
		return reverse('home')


""" Event Detail View """

class EventDetailView(DetailView):
	model = Event
	template_name = 'trucks/event_detail.html'


	def get_object(self, queryset=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		if slug:
			try:
				obj = self.model.objects.get(slug=slug)
			except self.model.MultipleObjectsReturned:
				obj = self.get_queryset().first()
			except:
				raise Http404
			return obj


""" Feedback Create View """
from django.contrib.auth.decorators import login_required
class CreateFeedbackView(SuccessMessageMixin, CreateView):
	model = Feedback
	fields = ['positive' ,'negative', 'suggestions']
	template_name = 'trucks/truckpremium_detail.html'


	def get_success_url(self):
		messages.success(self.request, "Feedback successfully added")
		return self.food_truck.get_absolute_url()

	@cached_property
	def food_truck(self):
		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])

	def form_valid(self, form):
		feedback = form.save(commit=False)
		feedback.food_truck = self.food_truck
		feedback.user = self.request.user
		if Feedback.objects.count() % 5 == 0:
			owner_email = feedback.food_truck.owner.email
			slug = feedback.food_truck.slug
			template = get_template('trucks/feedback_template.txt')
			context = Context({
			'owner_email':feedback.food_truck.owner.email,
			'slug':feedback.food_truck.slug,})
			content = template.render(context)
			email = EmailMessage('You have new feedback!', content, "WheelDine <hello@wheeldine.com",
			[owner_email], reply_to=['hello@wheeldine.com'])
			email.send()
			feedback.save()
		else:
			feedback.save()
		return super(CreateFeedbackView, self).form_valid(form)

""" Feedback Detail View """
class FeedbackDetailView(DetailView):
	model = Feedback
	template_name = 'trucks/feedback_detail.html'

	def get_object(self):
		return get_object_or_404(PlusTruck, slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(FeedbackDetailView, self).get_context_data(**kwargs)
		return context


""" About Page """

def AboutView(request):
	return render(request, 'trucks/about.html')

""" Pricing Page """

def PricingView(request):
	return render(request, 'trucks/pricing.html')

""" Terms of Service Page """

def ToSView(request):
	return render(request, 'trucks/tos.html')

""" Privacy Policy Page """

def PrivacyPolicyView(request):
	return render(request, 'trucks/privacy_policy.html')
