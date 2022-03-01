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
    path("stats/best_laptops", views.best_laptops),
    path("stats/best_companies", views.best_companies_2),
    path("stats/best_customers", views.best_customers),
    path("stats/customers_reviewed_all_laptops", views.customers_reviewed_all_laptops),
    path("stats/cheapest_not_reviewed_laptops", views.cheapest_not_reviewed_laptops),
    path("stats/cheapest_laptops_best_reviews", views.cheapest_laptops_best_reviews),
]