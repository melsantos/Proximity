from entry.forms import CustomUserCreationForm, CustomForgotUsernameForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        # Automatically signs the user in
        if form.is_valid():
            user = form.save()
            user.profile.age = form.cleaned_data.get('age')
            user.profile.save()
            user.save()
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            user.email_user(
                subject='Welcome to iLonely!',
                message = 'Hi %s! We hope you\'ll enjoy iLonely!' % user.get_username()
            )
            return render(
                request,
                'registration/success.html',
                {
                    'title':'Sucessful Login'
                }
            )
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        'registration/register.html',
        {
            'title':'Registration',
            'form':form,
        }
    )

def login_view(request):
    assert isinstance(request, HttpRequest)

    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            # Take user to their home page
            return redirect('user_home') 
    else:
        form = AuthenticationForm()
    return render(
        request,
        'registration/login.html',
        {
            'title':'Login',
            'form':form,
        }
    )

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return

def forgot_username_view(request):
    assert isinstance(request, HttpRequest)
    confirm = False
    if request.method == 'POST':
        form = CustomForgotUsernameForm(data=request.POST)
        if form.is_valid:
            confirm = True
            try:
                user = User.objects.filter(email=form['email']).first()
            except User.DoesNotExist:
                user = None
            if user is not None:
                user.email_user(
                    subject='iLonely: Account Username',
                    message = 'Did you forget your username? Don\'t worry, we didn\'t. Your username is: %s' % user.get_username()
                )
    else:
        form = CustomForgotUsernameForm()
    return render(
        request,
        'registration/forgot_username.html',
        {
            'title':'Forgot Username',
            'form': form,
            'confirm': confirm,
            'confirmation_message': 'We sent an email with your username to your account'
        }
    )

@login_required(login_url="home")
def success(request):
    return render(
        request,
        'registration/success.html',
        {
            'title':'Sucessful Login'
        }
    )