from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('form/', views.form, name='form'),
    path('index/', views.index),
    path('edit/<int:person_id>/', views.edit_person, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]