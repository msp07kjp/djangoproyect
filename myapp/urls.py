from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('proyect/', views.proyect, name='proyect'),
    path('task/<int:id>', views.task, name='task'),

]