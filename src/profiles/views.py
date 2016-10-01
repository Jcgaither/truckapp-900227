from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile
from trucks.models import PlusTruck
from actstream.models import following, followers
from actstream.actions import follow, unfollow
from django.template import RequestContext


User = get_user_model()

@login_required
def profile_view(request):
	user = get_object_or_404(User, username=request.user)
	profile, created = Profile.objects.get_or_create(user=user)
	owned = PlusTruck.objects.filter(owner=request.user)
	follow = following(request.user)
	context = {"profile": profile, "owned":owned, "follow": follow,}

	

	return render(request, 'profiles/profile.html', context,  context_instance=RequestContext(request))


# def recent_posts_view(request):
# 	if follow:
# 		recent_post = Statusupdate.objects.all().order_by('-id')[:20]
# 		context = {}


# class OwnedTrucks(TemplateView):
# 	model = TruckPremium
#  	template_name = 'trucks/profile.html'

#  	def get_context_data(self, **kwargs):
#  		context = super(OwnedTrucks, self).get_context_data(**kwargs)
#  		context['recent_trucks'] = Truck.objects.all().order_by('-id')[:20]	
#  		return context 
# def owned_trucks(self, request):
# 	if request.user.is_superuser:
# 		return truck_name.objects.all()
#     return truck_name.objects.filter(owner=request.user)