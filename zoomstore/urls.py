from django.urls import path
from . import views

# Url configuration.
urlpatterns = [
    path('store/', views.search),
    path('result/', views.search_result, name='result')
]
