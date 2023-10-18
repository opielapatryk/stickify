from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm
from django.views import generic 
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# your board
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context={})
    else:
        return HttpResponseRedirect(reverse("login"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

class Register(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'

# settings
def settings(request):
    return render(request, 'settings.html', context={})

# your friend board
def friend(request):
    return render(request, 'friend.html', context={})

# list your friends
def friends(request):
    return render(request, 'friends.html', context={})