from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from core.models import Customer

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard upon successful login
            return redirect('dashboard')
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid username or password.')
    # Render the login form
    return render(request, 'adminside/adminlogin.html')


def users(request):
    return render(request,'adminside/users.html')

@login_required
def dashboard(request):
    # Set session data
    request.session['user_id'] = request.user.id
    request.session['username'] = request.user.username
    return render(request, 'adminside/dashboard.html')


def users(request):
     users = Customer.objects.all()
     context = {
            'users': users,
        }
     return render(request,'adminside/users.html',context)

    