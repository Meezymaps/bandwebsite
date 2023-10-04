from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Event

# View requiring login to access
@login_required(login_url="/authentication/login/")
def home(request):
    """
    Render the home page.

    This view requires the user to be logged in.
    """
    return render(request, 'band/home.html')

def about(request):
    """
    Render the about page.
    """
    return render(request, 'band/about.html')

def events(request):
    """
    Render the events page with a list of all events.

    Retrieves all Event objects from the database and passes them to the template.
    """
    events = Event.objects.all()
    return render(request, 'band/events.html', {'events': events})

def signup(request):
    """
    Handle user registration.

    If the request method is POST, it processes the registration form.
    If the form is valid, it creates a new user and logs them in.
    If the method is GET, it displays the registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page or perform other actions as needed.
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})


