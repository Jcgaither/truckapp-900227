from rest_framework import serializers, viewsets, generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from trucks.models import BaseTruck, PlusTruck, Event
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.conf import settings


User = settings.AUTH_USER_MODEL


class PlusTruckSerializer(GeoFeatureModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = PlusTruck
		geo_field = "geom"
		fields = ('id','plus_truck_name','owner','plus_address', 'plus_city', 'plus_state', 'plus_thumbnail', 'urllink', 'slug',)


class PlusTruckViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = PlusTruck.objects.all()
	serializer_class = PlusTruckSerializer


class BaseTruckSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = BaseTruck
		geo_field = "geom"
		fields = ('base_truck_name', 'base_address', 'base_city', 'base_state',)


class BaseTruckViewSet(viewsets.ModelViewSet):
	queryset = BaseTruck.objects.all()
	serializer_class = BaseTruckSerializer


class EventSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Event
		geo_field = "event_geom"
		fields = ('event_name', 'event_address', 'event_city', 'event_state', 'event_thumbnail', 'urllink', 'slug',)

class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
