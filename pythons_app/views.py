from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from pythons_auth.models import UserProfile
from .forms import PythonCreateForm
from .models import Python


# Create your views here.



def index(request):
    user = request.user
    users = User.objects.all()
    pythons = Python.objects.all()
    user_profiles = UserProfile.objects.all()
    context = {
        'pythons': pythons,
        'users': users,
        'user_profiles': user_profiles,

    }
    return render(request, 'index.html', context)


@login_required(login_url='login_user')
def create(request):
    user = request.user
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            python = form.save(commit=False)
            python.creator = user
            python.save()
            return redirect('index')
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'create.html', context)


def all_users(request):
    template = 'all_users.html'
    all_users = User.objects.all()
    all_profiles = UserProfile.objects.all()
    context = {
        'all_users': all_users,
        'all_profiles': all_profiles,
    }
    return render(request, template, context)
