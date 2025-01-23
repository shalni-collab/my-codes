from django.shortcuts import render,redirect
from school.models import Contact

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # Import the form we just created

from .models import *
def home(request):

    return render(request,"index.html")
def aboutus(request):
    return render(request,"about.html")    
def contact(request):
    if request.method == "Post":
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        contact=Contact(name="name",mobile_number="mobile_number")
        contact.save()
    return render(request,"contact.html")
def events(request):
    return render(request,"events.html")    
def stuLogin(request):
       if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/stuLogin')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/stuLogin')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
    
    # Render the login page template (GET request)
       return render(request, 'stuLogin.html')
    
    
def studentadmin(request):
     if request.user.is_anonymous:
        return redirect("/stuLogin") 
    
     return render(request,"admin.html")

def student(request):
    return render(request,'student.html')
def director(request):
    return render(request,'director.html')
def teachers(request):
    return render(request,'teachers.html')
def signup(request):
     if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('blog-home') # Redirect user to Homepage
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    return render(request,'signup.html')
    
# Create your views here.
