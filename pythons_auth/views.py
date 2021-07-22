from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from pythons_auth.forms import RegisterForm, ProfileForm, LoginForm


@transaction.atomic
def register_user(request):
    template = 'auth/register.html'
    if request.method == "GET":
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, template, context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            group = Group.objects.get(name='Regular user')
            user.groups.add(group)
            pic = 'profile_image'
            if pic in request.FILES:
                profile.profile_image = request.FILES[pic]
            profile.save()
            registered = True
            login(request, user)
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, template, context)


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'



def login_user(request):
    template = 'auth/login.html'
    if request.method == "GET":
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }
        return render(request, template, context)
    else:
        login_form = LoginForm(request.POST)
        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(return_url)
        context = {
            'login_form': LoginForm(),
        }
        return render(request, template, context)


def logout_user(request):
    logout(request)
    return redirect('index')
