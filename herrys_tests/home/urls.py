from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('über/', views.ueber, name='über'),
    path('impressum/', views.impressum, name='impressum')
]
