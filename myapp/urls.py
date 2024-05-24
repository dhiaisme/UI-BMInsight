from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-copy/', views.index_copy, name='index_copy'),
    path('about/', views.about, name='about'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('dataset-example/', views.example, name='dataset_example'),
    path('contact/', views.contact, name='contact'),
    path('department-single/', views.department_single, name='department_single'),
    path('department/', views.department, name='department'),
    path('documentation/', views.documentation, name='documentation'),
    path('services/', views.services, name='services'),
]
