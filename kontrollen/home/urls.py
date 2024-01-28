from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('über/', views.über, name='über'),
    path('impressum/', views.impressum, name='impressum'),
    path('datenschutzerklärung/', views.datenschutzerklärung, name='datenschutzerklärung')
]
