from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Profile, Business, Post 



# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

