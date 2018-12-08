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
# import marketplace.urls

# enables admin site
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from postman.views import WriteView

admin.autodiscover()

urlpatterns = [
    url(r'^$', pages.views.home, name='home'),
    url(r'^register$', pages.views.register, name='register'),

    url(r'^login$', pages.views.login_view, name='login'),
    url('logout$', pages.views.logout_view, name='logout'),
    path('forgot_username', pages.views.forgot_username_view, name='forgot_username'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^success$', pages.views.success, name='success'),
    url(r'^user_home/$', pages.views.user_home_view, name='user_home'),
    url(r'^set_location$', pages.views.set_location, name='set_location'),
    url(r'^notifications$', pages.views.notifications_view, name='notifications'),
    # url(r'^view_following$', pages.views.view_following, name='view_following'),
    url(r'^view_nearby$', pages.views.view_nearby, name='view_nearby'),
    url(r'^public_profile/(?P<userid>\d+)/$', pages.views.public_profile, name='public_profile'),
    # url(r'^my_profile/$', pages.views.my_profile, name='my_profile'),
    url(r'^account/$', pages.views.account, name='account'),
    url(r'^feed$', pages.views.user_home_view, name='feed'),
    url(r'^admin/', admin.site.urls), # admin site url
    url(r'^messages/', include('postman.urls', namespace='postman')),
    url(r'auth/', include('social_django.urls', namespace='social')),
    url(r'^events/(?P<activeEventId>\d+)/$', pages.views.events, name='events'),
    path(r'marketplace/', include('marketplace.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
