from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from trucks.models import PlusTruck, BaseTruck, Event
from trucks import json_views
from actstream import views
from trucks.serializers import PlusTruckViewSet, BaseTruckViewSet, PlusTruckImageViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"plustrucks", PlusTruckViewSet,)
router.register(r"basetrucks", BaseTruckViewSet,)
router.register("images", PlusTruckImageViewSet, "images")
admin.autodiscover()

import permission; permission.autodiscover()

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^063093227900/', include(admin.site.urls)),
    url(r'', include('trucks.urls')),
    url(r'^contact/', include('envelope.urls')),
    url(r'', include('profiles.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^payments/', include('djstripe.urls', namespace='djstripe')),
    url('^activity/', include('actstream.urls')),
    url(r'^follow/(?P<slug>[-\w]+)/',
        views.follow_unfollow, name='actstream_follow'),
    url(r'^unfollow/(?P<slug>[-\w]+)/',
        views.follow_unfollow, name='actstream_unfollow'),
    url(r'^premiumdata.geojson/', json_views.PlusTruckMapCollection.as_view(), name='premium_data'),
    url(r'^truckdetail.json/$', json_views.PlusTruckList.as_view(), name='ptl'),
    url(r'^truckdetail.json/(?P<pk>[0-9]+)$', json_views.PlusTruckDetail.as_view(), name='ptd'),
    url(r'^basedata.geojson/$', json_views.BaseMapCollection.as_view(), name='base_data'),
    url(r'^eventdata.geojson/$', json_views.EventMapCollection.as_view(), name='event_data'),
    url(r'^eventdetail.json/$', json_views.EventList.as_view(), name='evl'),
    url(r'^eventdetail.json/(?P<pk>[0-9]+)$', json_views.EventDetail.as_view(), name='evd'),
    url(r'^api/auth/', include("rest_framework.urls", namespace='rest_framework')),
    url(r'^api/', include(router.urls)),




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'truckapp.views.handler404'
handler500 = 'truckapp.views.handler500'
