from haystack import indexes
from trucks.models import PlusTruck, BaseTruck, Event


class PlusTruckIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	truck_name = indexes.CharField(model_attr='plus_truck_name')
	address = indexes.CharField(model_attr='plus_address')
	city = indexes.CharField(model_attr='plus_city')
	state = indexes.CharField(model_attr='plus_state')
	postal_code = indexes.CharField(model_attr='plus_postal_code')

	def get_model(self):
		return PlusTruck


class BaseTruckIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	truck_name = indexes.CharField(model_attr='base_truck_name')
	address = indexes.CharField(model_attr='base_address')
	city = indexes.CharField(model_attr='base_city')
	state = indexes.CharField(model_attr='base_state')
	postal_code = indexes.CharField(model_attr='base_postal_code')

	def get_model(self):
		return BaseTruck

class EventIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	event_name = indexes.CharField(model_attr='event_name')
	address = indexes.CharField(model_attr='event_address')
	city = indexes.CharField(model_attr='event_city')
	state = indexes.CharField(model_attr='event_state')
	postal_code = indexes.CharField(model_attr='event_postal_code')

	def get_model(self):
		return Event
