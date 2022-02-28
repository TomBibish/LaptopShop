from django.urls import path
from . import views
from datetime import date
from datetime import datetime
urlpatterns = [
    path('laptops', views.laptops, name='laptops'),
    path("laptops/<int:pk>", views.laptop_details),
    path('orders', views.orders, name='orders'),
    path("orders/<int:pk>", views.order_details),
    path("best_5_laptops", views.best_5_laptops),
    path("best_companies", views.best_companies),
    path("total_sales_by_date/<str:first_date>,<str:end_date>", views.total_sales_by_date),
    path('reviews', views.reviews, name='reviews'),
    path("reviews/<int:pk>", views.review_details),
]