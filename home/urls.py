from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('review_add/', views.review_add, name='review_add'),
]
