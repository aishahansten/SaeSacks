from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'), 
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
