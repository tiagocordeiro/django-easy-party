from django.urls import path

from . import views

urlpatterns = [
    path('invites/', views.invites_list, name='invites_list'),
    path('invite/create/', views.invite_create, name='invite_create'),
    path('invite/share/<pk>/', views.invite_share, name="invite_share"),
    path('invite/public/<pk>/', views.invite_public, name="invite_public"),
    path('invite/update/<pk>/', views.invite_update, name='invite_update'),
    path('invite/download/<pk>/', views.invite_download_jpg, name='invite_download_jpg')
]
