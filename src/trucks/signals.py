from django.db.models.signals import post_save
from actstream import action
from trucks.models import PlusTruck
from actstream.actions import follow, unfollow
from actstream.models import actor_stream

plus_truck = PlusTruck.objects.get(name='truck')

# truck = PremiumTruckLocation.objects.get()
# action.send(request.user, verb="followed", target=truck)
# action.send(request.user, verb="posted")
actor_stream(truck)
follow(request.user, truck, verb='visited' actor_only=False)
unfollow(request.user, truck, actor_only=False)


# user_stream(request.user, with_user_activity=True)