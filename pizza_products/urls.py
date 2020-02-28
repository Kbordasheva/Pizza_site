from django.urls import path, include
from pizza_products import views

urlpatterns = [
    path('', views.home, name='home'),
]