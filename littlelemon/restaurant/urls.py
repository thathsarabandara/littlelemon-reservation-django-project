from django.contrib import admin 
from django.urls import path 
from .views import BookingView, MenuView 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('', views.home),
    path('menu/<int:pk>',MenuView.as_view()), 
    path('booking/',BookingView.as_view()), 
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]