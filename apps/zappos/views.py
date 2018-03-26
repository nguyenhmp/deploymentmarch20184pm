# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    context = {
        "all_users":User.objects.all()
    }
    return render(request, "zappos/users/index.html", context)
def users_index(request):
    context = {
        "all_users":User.objects.all()
    }
    return render(request, "zappos/users/index.html", context)
def users_create(request):
    User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"])
    return redirect("/zappos/users")