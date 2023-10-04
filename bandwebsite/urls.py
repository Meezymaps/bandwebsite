# Import necessary modules from Django
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

# Import views from the 'band' app
from band import views

# Define the URL patterns for your Django project
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Include authentication-related URLs from the 'authentication' app
    path('authentication/', include('authentication.urls')),

    # Include 'band' app URLs under 'rr' path
    path('00/', include('band.urls')),

    # Include authentication-related URLs as the default route
    path('', include('authentication.urls')),
]

