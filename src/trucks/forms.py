from django import forms
import geocoder
from trucks.models import BaseTruck, DeleteRequest, PlusTruck, EmailCollection, Event, Feedback
from localflavor.us.forms import USStateField
from django.forms.models import modelformset_factory
from django.conf import settings

class BaseTruckCreateForm(forms.ModelForm):

	class Meta:
		model = BaseTruck
		fields = (
			'base_truck_name',
			'base_address',
			'base_city',
			'base_state',
			'base_postal_code',
			'base_food_type',
			)


class BaseDeleteRequest(forms.ModelForm):

	class Meta:
		model = DeleteRequest
		fields = (
			'email',
			'truck',
			'reason',
			)

class PlusTruckCreateForm(forms.ModelForm):

	class Meta:
		model = PlusTruck
		fields = (
			'plus_truck_name',
			'plus_email',
			'plus_address',
			'plus_city',
			'plus_state',
			'plus_postal_code',
			'plus_menu',
			'plus_menu_photo',
			'plus_food_type',
			'plus_description',
			'plus_thumbnail',
			# 'plus_status',
			# 'top_truck',
			)
class PlusTruckUpdateForm(forms.ModelForm):

	# open_time = forms.TimeField(input_formats=settings.TIME_INPUT_FORMATS)
	# close_time = forms.TimeField(input_formats=settings.TIME_INPUT_FORMATS)

	class Meta:
		model = PlusTruck
		fields = ('plus_truck_name',
		          'plus_address',
		          'plus_city',
		          'plus_email',
		          'plus_state',
		          'plus_postal_code',
		          'plus_description',
		          'plus_status',
		          'plus_food_type',
		          'plus_menu',
		          'plus_menu_photo',
		          'plus_thumbnail',
		          'open_time',
		          'close_time',)


class EmailCollectionForm(forms.ModelForm):

	class Meta:
		model = EmailCollection
		fields = ('email', )

class EventCreateForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = (
			'event_name',
			'event_address',
			'event_city',
			'event_state',
			'event_postal_code',
			'event_description',
			'event_start_date',
			'event_end_date',
			)

class FeedbackForm(forms.ModelForm):

	class Meta:
		model = Feedback
		fields = (
			'food_truck',
			'positive',
			'negative',
			'suggestions',
			)
