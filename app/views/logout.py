from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout as django_logout
from django.conf import settings

 
@login_required
def logout(request):
   django_logout(request)
   domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
   client_id = settings.SOCIAL_AUTH_AUTH0_KEY
   return_to = 'http://127.0.0.1:8000' # this can be current domain
   return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')