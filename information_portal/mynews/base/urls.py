from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),# Home view
    path('news/<str:category>/', views.news_category, name='category_news'),  # Category view
]