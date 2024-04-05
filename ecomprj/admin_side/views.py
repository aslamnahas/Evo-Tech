from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from core.models import Customer
from core.models import Main_Category

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

    

def main_category(request):
    data = Main_Category.objects.all().order_by('id')
    return render(request, "adminside/categories.html", {"data": data})

def add_main_category(request):
    if request.method == 'POST':
        main_category_name = request.POST.get('main_category_name')
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        image = request.FILES.get('image')
        delete = request.POST.get('delete', False) == 'True'
        
        # Check if the category name already exists
        if Main_Category.objects.filter(name=main_category_name).exists():
            messages.error(request, "Category already exists.")
            return redirect('adminside:add_categories')  # Redirect to the add_main_category page
            
        # Save data to the database
        main_category = Main_Category(
            name=main_category_name,
            descriptions=description,
            offer=offer,
            img=image,
            deleted=delete
        )
        main_category.save()
        messages.success(request, "Category added successfully.")
        return redirect('adminside:categories')  # Redirect to the main_category page
    return render(request, 'adminside/add_categories.html')
