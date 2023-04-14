from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_company', views.all_company, name='all_company'),
    path('all_device', views.all_device, name='all_device'),
    path('company_details/<int:company_id>/', views.company_details, name='about_company'),
    path('device_details/<int:device_id>/', views.device_details, name='about_device'),
]
