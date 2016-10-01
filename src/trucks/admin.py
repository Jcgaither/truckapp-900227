from django.contrib import admin
from trucks.models import BaseTruck, DeleteRequest, PlusTruck, EmailCollection, Event, Feedback
from trucks.forms import BaseTruckCreateForm, BaseDeleteRequest, PlusTruckCreateForm, EmailCollectionForm, EventCreateForm, FeedbackForm
from profiles.models import Profile

class TruckAdmin(admin.ModelAdmin):
	form = BaseTruckCreateForm

class TruckPremiumAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		TruckPremium.owner = request.user
		TruckPremium.save()

class TruckDeleteRequest(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		BaseDeleteRequest.user = request.user
		BaseDeleteRequest.save()


class TestAdminCoords(admin.ModelAdmin):
	form = PlusTruckCreateForm

class EmailCollectionAdmin(admin.ModelAdmin):
	form = EmailCollectionForm

class EventAdmin(admin.ModelAdmin):
	form = EventCreateForm


class FeedbackAdmin(admin.ModelAdmin):
	form = FeedbackForm


admin.site.register(BaseTruck, TruckAdmin)
admin.site.register(DeleteRequest, TruckDeleteRequest)
admin.site.register(PlusTruck, TestAdminCoords)
admin.site.register(EmailCollection, EmailCollectionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Feedback, FeedbackAdmin)
