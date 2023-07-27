from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('proyect/', views.proyect, name='proyect'),
    path('task/', views.task, name='task'),
    path('about/', views.about, name='about'),
    path('crud/create_task/', views.create_task, name='create_task'),


    path('hello/<str:username>', views.hello, name='hello'),

]