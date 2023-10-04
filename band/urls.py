
from django.urls import path
from . import views

# Define the URL patterns for your application
urlpatterns = [
    # URL for the home page, mapped to the 'home' view function
    path('', views.home, name='home'),
    # URL for the about page, mapped to the 'about' view function
    path('about/', views.about, name='about'),
    # URL for the events page, mapped to the 'events' view function
    path('events/', views.events, name='events'),
]




