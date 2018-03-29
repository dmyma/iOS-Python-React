from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from foodtaskerapp.forms import UserForm, RestaurantForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.model import User

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})
