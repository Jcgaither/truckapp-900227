from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views
from .views import (TruckHomeView, TruckCreateView, TruckDeleteView, PlusTruckCreateView, PlusTruckDeleteView,
PlusTruckUpdateView, PlusTruckDetailView, MapView, FormSelectView, RankView,
EventCreateView, EventDetailView, CreateFeedbackView, FeedbackDetailView, AboutView, PricingView, ToSView, PrivacyPolicyView)

urlpatterns = [
   url(r'^$', 'trucks.views.TruckHomeView', name='home'),
   url(r'^add/foodtruck/$', TruckCreateView.as_view(), name='base_truck_create'),
   url(r'^(?P<slug>[-\w]+)/delete/$', PlusTruckDeleteView.as_view(), name='plus_truck_delete'),
   url(r'^(?P<slug>[-\w]+)/update/$', PlusTruckUpdateView.as_view(), name='plus_truck_update'),
   url(r'^(?P<slug>[-\w]+)$', PlusTruckDetailView.as_view(), name='plus_truck_detail'),
   url(r'^map/$', MapView.as_view(), name='map'),
   url(r'^tos/$', 'trucks.views.ToSView', name='tos'),
   url(r'^privacypolicy/$', 'trucks.views.PrivacyPolicyView', name='privacy_policy'),
   url(r'^about/$', 'trucks.views.AboutView', name='about'),
   url(r'^premium/$', 'trucks.views.PricingView', name='pricing'),
   url(r'^add/plustruck/$', PlusTruckCreateView.as_view(), name='plus_truck_create'),
   url(r'^add/$', 'trucks.views.FormSelectView', name='select_form'),
   url(r'^deleterequest/$', TruckDeleteView.as_view(), name='delete_trucks'),
   url(r'^recent-activity/$', 'trucks.views.RankView', name='truck_ranking'),
   url(r'^add/event/$', EventCreateView.as_view(), name='event_create'),
   url(r'^event/(?P<slug>[-\w]+)$', EventDetailView.as_view(), name='event_detail'),
   url(r'^(?P<slug>[-\w]+)$', PlusTruckDetailView.as_view(), name='plus_truck_detail'),
   url(r'^(?P<slug>[-\w]+)/addfeedback/$', CreateFeedbackView.as_view(), name='add_feedback'),
   url(r'^(?P<slug>[-\w]+)/feedback/$', FeedbackDetailView.as_view(), name='feedback'),

   ]
