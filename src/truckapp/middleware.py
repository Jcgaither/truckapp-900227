# from django.conf import settings
# from django.contrib import messages
# from django.core.urlresolvers import reverse
# from django.shortcuts import HttpResponseRedirect



# URLS = [reverse(url) for url in settings.SUBSCRIPTION_REQUIRED_URLS]

# class CheckMembership():
#     def process_request(self, request):
#         if request.user.is_authenticated():
#             if request.path in URLS:
#                 role = request.user.userrole
#                 if request.user.paid_member = True
#                 message.success(request, 'Subscription required!')
#                 return HttpResponseRedirect('stripe_subscription')
#         else:
#             messages.error(request, 'user is not logged in')