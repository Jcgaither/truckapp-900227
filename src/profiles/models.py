from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return self.user.username

	def get_absolute_url(self):
		url = reverse("profile", kwargs={"username": self.user.username})
		return url