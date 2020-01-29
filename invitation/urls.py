from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_invites, name='list_invites'),
    path('download/<pk>/', views.download_invite, name='download_invite')
]
