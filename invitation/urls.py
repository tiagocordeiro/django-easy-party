from django.urls import path

from . import views

urlpatterns = [
    path('', views.invites_list, name='invites_list'),
    path('download/<pk>/', views.invite_download_jpg, name='invite_download_jpg')
]
