from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('insert_district/', views.insert_district, name = 'insert_district'),
    path('search_district/', views.search_district, name = 'search_district'),
    path('update_district/', views.update_district, name = 'update_district'),
    path('delete_district/', views.delete_district, name = 'delete_district'),
    path('insert_crime/', views.insert_crime, name = 'insert_crime'),
    path('search_crime/', views.search_crime, name = 'search_crime'),
    path('update_crime/', views.update_crime, name = 'update_crime'),
    path('delete_crime/', views.delete_crime, name = 'delete_crime'),
]
