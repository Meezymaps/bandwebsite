
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView

# Custom LoginView class to specify a custom template
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# View for handling user login
def login_view(request):
    if request.method == 'POST':
        # Create an AuthenticationForm instance with user input data
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Log the user in and redirect to the 'home' page
                login(request, user)
                return redirect('home')
            else:
                # Display an error message for invalid credentials
                messages.error(request, 'Invalid username or password.')
        else:
            # Display an error message for invalid form data
            messages.error(request, 'Invalid username or password.')
    else:
        # Create a new empty AuthenticationForm for GET requests
        form = AuthenticationForm()
    
    # Render the login template with the form
    return render(request, 'login.html', {'form': form})

# View for user registration
def register_view(request):
    if request.method == 'POST':
        # Create a UserCreationForm instance with user input data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user registration data
            form.save()
            username = form.cleaned_data.get('username')
            
            # Display a success message for successful registration
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        # Create a new empty UserCreationForm for GET requests
        form = UserCreationForm()
    
    # Render the registration template with the form
    return render(request, 'register.html', {'form': form})

# View for user logout
def logout_view(request):
    # Log the user out and redirect to the 'login' page
    logout(request)
    return redirect('login')
