from django.conf.urls import include, url
from django.contrib import admin
from profiles.views import profile_view

urlpatterns = [
	#url(r'^profile/(?P<username>[\w.@+-]+)/$', 'profiles.views.profile_view', name='profile'),
	url(r'^profile/$', 'profiles.views.profile_view', name='profile'),
]
