from rest_framework import serializers, viewsets, generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from trucks.models import BaseTruck, PlusTruck, Event, PlusTruckImage
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

class PlusTruckImageSerializer(serializers.ModelSerializer):
	food_truck = PlusTruckSerializer(read_only=True, required=False)
	class Meta:
		model  = PlusTruckImage
		fields = ('pk', 'food_truck', 'file',)

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(PlusTruckImageSerializer, self).get_validation_exclusions()

		return exclusions + ['food_truck']

class PlusTruckImageViewSet(viewsets.ModelViewSet):
	queryset = PlusTruckImage.objects.all()
	serializer_class = PlusTruckImageSerializer

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
