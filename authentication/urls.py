# authentication/urls.py

from django.urls import path
from . import views

# URL patterns for authentication-related views
urlpatterns = [
    # URL for the login view, mapped to the 'login_view' function
    path('', views.login_view, name='login'),

    # URL for the registration view, mapped to the 'register_view' function
    path('register/', views.register_view, name='register'),

    # URL for the logout view, mapped to the 'logout_view' function
    path('logout/', views.logout_view, name='logout'),
]

