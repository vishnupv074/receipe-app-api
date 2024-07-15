"""
URL mappings for the user API.
"""
from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='user-create'),
    path('token/', views.CreateTokenView.as_view(), name='user-token'),
    path('me/', views.ManageUserView.as_view(), name='user-me'),
]
