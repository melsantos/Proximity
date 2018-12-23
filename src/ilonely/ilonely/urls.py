"""
Definition of urls for ilonely.
"""

from datetime import datetime
from django.conf.urls import include, url
from django.urls import path, include
from django.contrib.auth import views

import django.contrib.auth.views
import django.contrib.auth.urls
import pages.views
import postman.views
import entry.views

# enables admin site
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from postman.views import WriteView
from pages.forms import CustomWriteForm

admin.autodiscover()

urlpatterns = [
    'postman.views',
    url(r'^write/(?:(?P<recipients>[^/#]+)/)?$',
        WriteView.as_view(form_classes=(CustomWriteForm)),
        name='write'),
]

urlpatterns = [
    url(r'^$', pages.views.home, name='home'),
    url(r'^user_home/$', pages.views.user_home_view, name='user_home'),
    url(r'^set_location$', pages.views.set_location, name='set_location'),
    url(r'^notifications$', pages.views.notifications_view, name='notifications'),
    url(r'^view_nearby$', pages.views.view_nearby, name='view_nearby'),
    url(r'^public_profile/(?P<userid>\d+)/$', pages.views.public_profile, name='public_profile'),
    url(r'^account/$', pages.views.account, name='account'),
    url(r'^feed$', pages.views.user_home_view, name='feed'),
    url(r'^admin/', admin.site.urls), # admin site url
    url(r'^messages/', include('postman.urls', namespace='postman')),
    url(r'auth/', include('social_django.urls', namespace='social')),
    url(r'^events/(?P<activeEventId>\d+)/$', pages.views.events, name='events'),
    path(r'marketplace/', include('marketplace.urls')),
    path(r'', include('entry.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
