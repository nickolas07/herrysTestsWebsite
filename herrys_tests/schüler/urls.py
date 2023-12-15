from django.urls import path
from . import views

urlpatterns = [
    path('', views.erstellen, name='erstellen'),
    path('<int:jahrgang>/', views.erstellen, name='erstellen'),
    path('pdf/<str:test_name>/', views.view_pdf, name='pdf'),
    path('download/<str:test_name>/', views.download_pdf, name='download_pdf')
]
