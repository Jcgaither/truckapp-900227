from rest_framework import mixins, generics, permissions
from rest_framework.generics import (
	ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from trucks import models, serializers
from trucks.models import PlusTruck, Event
from trucks.permissions import IsOwnerOrReadOnly

class PlusTruckMixin(object):
	queryset = PlusTruck.objects.all()
	serializer_class = serializers.PlusTruckSerializer
	permission_classes = (IsOwnerOrReadOnly,)


class EventMixin(object):
	queryset = Event.objects.all()
	serializer_class = serializers.EventSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PlusTruckMapCollection(PlusTruckMixin, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

	def get(self,request):
		return self.list(request)

	def post(self,request):
		return self.create(request)

class PlusTruckMember(generics.RetrieveUpdateDestroyAPIView):
	queryset = PlusTruck.objects.all()
	serializer_class = serializers.PlusTruckSerializer
	permission_classes = (IsOwnerOrReadOnly, )


	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)



class PlusTruckList(PlusTruckMixin, ListCreateAPIView):
	pass

class PlusTruckDetail(PlusTruckMixin, RetrieveUpdateDestroyAPIView):
	pass

class BaseMapCollection(generics.ListAPIView):
	queryset = models.BaseTruck.objects.all()
	serializer_class = serializers.BaseTruckSerializer


class EventMapCollection(generics.ListAPIView):
	queryset = models.Event.objects.all()
	serializer_class = serializers.EventSerializer

class EventList(EventMixin, ListCreateAPIView):
	pass

class EventDetail(EventMixin, RetrieveUpdateDestroyAPIView):
	pass
