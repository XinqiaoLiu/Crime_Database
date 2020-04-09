from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('district/', views.insert_district, name = 'district'),
]
