from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from foodtaskerapp.forms import UserForm, RestaurantForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.model import User

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
