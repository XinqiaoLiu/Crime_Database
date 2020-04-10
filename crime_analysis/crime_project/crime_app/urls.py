from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('insert_district/', views.insert_district, name = 'insert_district'),
    path('search_district/', views.search_district, name = 'search_district'),
    path('update_district/', views.update_district, name = 'update_dsitrict'),
    path('delete_district/', views.delete_district, name = 'delete_district'),
]
