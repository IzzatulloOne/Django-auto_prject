from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('brand/<int:brand_id>/', views.brand_category, name='brand_category'),
]
