from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/upvote', views.upvote, name='upvote')
]
