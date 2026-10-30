from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    return render(request, 'register.html')

def add_report(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        report_type = request.POST.get('report_type') == 'True'  # Convert to boolean
        description = request.POST.get('description')
        location = request.POST.get('location')
        status = request.POST.get('status') == 'True'  # Convert to boolean
        
        # Create a new LostFoundReport object and save it to the database
        report = LostFoundReport(
            item_name=item_name,
            report_type=report_type,
            description=description,
            location=location,
            status=status,
            reported_by=request.user  # Set the reported_by field to the current user
        )
        report.save()
        
        return redirect('/home/')  # Redirect to the home page after adding the report
    
    return render(request, 'add_report.html')       

def edit_report(request, report_id):        
    report = LostFoundReport.objects.get(id=report_id)
    
    if request.method == 'POST':
        report.item_name = request.POST.get('item_name')
        report.report_type = request.POST.get('report_type') == 'True'  # Convert to boolean
        report.description = request.POST.get('description')
        report.location = request.POST.get('location')
        report.status = request.POST.get('status') == 'True'  # Convert to boolean
        
        report.save()  # Save the updated report to the database
        
        return redirect('/home/')  # Redirect to the home page after editing the report
    
    return render(request, 'edit_report.html', {'report': report})