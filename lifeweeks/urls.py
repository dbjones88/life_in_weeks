from django.urls import path
from lifeweeks import views

urlpatterns = [
    path('', views.home, name='home'), # "home" is the landing page   
]