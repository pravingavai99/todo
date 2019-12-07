from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='item'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
