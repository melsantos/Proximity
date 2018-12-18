from django.conf.urls import include, url
from django.urls import path, include
from django.contrib.auth import views
import entry.views

urlpatterns = [
    url(r'^register$', entry.views.register, name='register'),
    url(r'^login$', entry.views.login_view, name='login'),
    url('logout$', entry.views.logout_view, name='logout'),
    path('forgot_username', entry.views.forgot_username_view, name='forgot_username'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # url(r'^success$', entry.views.success, name='success'), # to check styling
]
