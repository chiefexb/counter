from django.conf.urls import url,include 
from django.urls import  path,re_path
from . import views
from counterdb.views import  counter
urlpatterns = [
    path("", views.index, name='index'),
    path('counter', views.counter),
    
    
]