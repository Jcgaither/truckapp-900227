from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.conf import settings
from profiles.models import Profile
import geocoder
from django.contrib.gis.db import models
from PIL import Image
from localflavor.us.models import USStateField, PhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
from sorl.thumbnail import ImageField
import itertools


User = settings.AUTH_USER_MODEL


class BaseTruck(models.Model):
	base_truck_name = models.CharField(max_length=200)
	base_address = models.CharField(max_length=500, blank=True)
	base_city = models.CharField(max_length=100)
	base_state = USStateField()
	base_postal_code = models.CharField(max_length=100, null=True)
	base_food_type = models.CharField(max_length=45, blank=True, null=True)
	geom = models.PointField(blank=True, srid=4326)
	created_date = models.DateTimeField(default=timezone.now)



	def save(self, *args, **kwargs):
		location = "%s, %s, %s, %s" % (self.base_address, self.base_city, self.base_state, self.base_postal_code)
		self.slug = slugify(self.base_truck_name)


		if not self.geom:
			points = geocoder.google(location)
			self.geom = points.wkt
		super(BaseTruck, self).save(*args, **kwargs)


	def __unicode__(self):
		return self.base_truck_name



class DeleteRequest(models.Model):
	user = models.ForeignKey(User, null=True)
	email = models.EmailField(default="Test", null=True)
	truck = models.CharField(max_length=250)
	reason = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email



class EmailCollection(models.Model):
	email = models.EmailField(max_length=75)

	def __unicode__(self):
		return self.email

#remove null=true for times, phone numbers,Switch timefiled to charfield)
class PlusTruck(models.Model):
	owner = models.ForeignKey(User, related_name="trucks")
	plus_truck_name = models.CharField(max_length=200)
	plus_address = models.CharField(max_length=200, blank=True)
	plus_city = models.CharField(max_length=100)
	plus_state = USStateField(choices=STATE_CHOICES)
	plus_postal_code = models.CharField(max_length=100, blank=True)
	geom = models.PointField(blank=True)
	plus_description = models.TextField(null=True, blank=True)
	plus_food_type = models.CharField(max_length=45, null=True, blank=True)
	plus_menu = models.TextField(null=True, blank=True)
	plus_menu_photo = models.ImageField(upload_to="images/", null=True, blank=True)
	plus_thumbnail = ImageField(upload_to="images/", null=True, blank=True)
	plus_phone_number = PhoneNumberField(null=True, blank=True)
	plus_email = models.EmailField(null=True, blank=True)
	open_time = models.CharField(max_length=15, blank=True, null=True)
	close_time = models.CharField(max_length=15, blank=True, null=True)
	plus_status = models.CharField(max_length=140, default='', null=True, blank=True)
	slug = models.SlugField()
	top_truck = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	urllink = models.CharField(max_length=150, blank=True)


	def __unicode__(self):
		return self.plus_truck_name

	@property
	def truck_image_url(self):
		if self.plus_thumbnail:
			return self.plus_thumbnail.url
		else:
			return '/static/img/plustruck.png'

	def save(self, *args, **kwargs):
		link = "www.wheeldine.com/"
		max_length = PlusTruck._meta.get_field('slug').max_length
		self.slug = orig = slugify(self.plus_truck_name)[:max_length]
		for x in itertools.count(1):
			if not PlusTruck.objects.filter(slug=self.slug).exists():
				break
			self.slug = '%s-%d' % (orig[:max_length - len(str(x)) -1], x)


		self.urllink = link + self.slug
		location = "%s, %s, %s, %s" % (self.plus_address, self.plus_city, self.plus_state, self.plus_postal_code)

		if not self.geom:
			points = geocoder.google(location)
			self.geom = points.wkt
		else:
			points = geocoder.google(location)
			self.geom = points.wkt

		try:
			this = PlusTruck.objects.get(slug=self.slug)
			if this.plus_thumnail != self.plus_thumbnail | this.plus_menu_photo != self.plus_menu_photo:
				this.plus_thumbnail.delete(save=False)
				this.plus_menu.delete(save=False)
		except: pass

		super(PlusTruck, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("plus_truck_detail", kwargs={'slug':self.slug})


from permission import add_permission_logic
from permission.logics import AuthorPermissionLogic
add_permission_logic(PlusTruck, AuthorPermissionLogic(
	field_name='owner',
	any_permission=False,
	change_permission=True,
	delete_permission=True
	))



class PlusTruckImage(models.Model):
	food_truck = models.ForeignKey(PlusTruck, blank=True, null=True, on_delete=models.SET_NULL)
	file = models.FileField(upload_to="images/%Y/%m/%d")

	def __unicode__(self):
		return self.file.url




class Event(models.Model):
	creator = models.ForeignKey(User)
	event_name = models.CharField(max_length=200)
	event_address = models.CharField(max_length=200, blank=True)
	event_city = models.CharField(max_length=100)
	event_state = USStateField(choices=STATE_CHOICES)
	event_postal_code = models.CharField(max_length=100, blank=True)
	event_geom = models.PointField(blank=True)
	event_description = models.TextField(null=True, blank=True)
	event_start_date = models.DateTimeField()
	event_end_date = models.DateTimeField(null=True, blank=True)
	event_thumbnail = ImageField(upload_to="images/", null=True, blank=True)
	slug = models.SlugField()
	urllink = models.CharField(max_length=150, blank=True)

	def __unicode__(self):
		return self.event_name


	def save(self, *args, **kwargs):
		link = "www.wheeldine.com/event/"
		max_length = Event._meta.get_field('slug').max_length
		self.slug = orig = slugify(self.event_name)[:max_length]
		for x in itertools.count(1):
			if not Event.objects.filter(slug=self.slug).exists():
				break
			self.slug = '%s-%d' % (orig[:max_length - len(str(x)) -1], x)


		self.urllink = link + self.slug
		location = "%s, %s, %s, %s" % (self.event_address, self.event_city, self.event_state, self.event_postal_code)



		if not self.event_geom:
			points = geocoder.google(location)
			self.event_geom = points.wkt
		super(Event, self).save(*args, **kwargs)

	@property
	def event_image_url(self):
		if self.event_thumbnail:
			return self.event_thumbnail.url
		else:
			return '/static/img/event_flag.png'

	def get_absolute_url(self):
		return reverse("event_detail", kwargs={'slug':self.slug})

""" Uncomment timestamp """
class Feedback(models.Model):
	user = models.ForeignKey(User)
	food_truck = models.ForeignKey(PlusTruck)
	positive = models.TextField(blank=True)
	negative = models.TextField(blank=True)
	suggestions = models.TextField(blank=True)
	timestamp = models.DateTimeField(default=timezone.now)


	def unicode(self):
		return self.food_truck

	def get_absolute_url(self):
		return reverse("plus_truck_detail", kwargs={'slug':self.slug})

add_permission_logic(Feedback, AuthorPermissionLogic(
	field_name='owner',
	any_permission=False,
	change_permission=True,
	delete_permission=True
	))
