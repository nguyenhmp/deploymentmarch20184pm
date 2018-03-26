from django.conf.urls import url, include
from django.contrib import admin
import views
# zappos/  
#     +users(zappos/users)
urlpatterns = [
    url(r'^users$', views.users_index),
    url(r'^users/create$', views.users_create)
]