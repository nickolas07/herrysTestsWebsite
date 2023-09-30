from django.urls import path
from . import views

urlpatterns = [
    path('', views.erstellen, name='home'),
    path('klasse/<int:jahrgang>/', views.erstellen_by_jahrgang, name='jg'),
    path('pdf/<str:test_name>/', views.view_pdf, name='pdf'),
    path('download/<str:test_name>/', views.download_pdf, name='download_pdf'),
    path('impressum/', views.impressum, name='impressum')
]
