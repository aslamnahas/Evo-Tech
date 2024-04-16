# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm, LoginForm
from core.models import Main_Category







def home(request):
    # signup(request)
    return render(request, "core/home.html")




###############################################################################
# user signup
###############################################################################

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            userss = form.save(commit=False)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            userss.set_password(password)
            userss.save()
            # Authenticate and log in the user
            userss = authenticate(email=email, password=password)
            if userss is not None:
                login(request, userss)
                return redirect('core:home')  # Redirect to your home page
    else:
        form = NewUserForm()
    return render(request, 'core/registration.html', {'form': form})

 


###########################################################################
# user login
##########################################################################

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)  # Authenticate the user
                return redirect('core:home')  # Redirect to the home page after login
    else:
        form = LoginForm()
    return render(request, 'core/userlogin.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('core:home') 

def google(request):

      context = {
        'provider': 'Google'  # You can dynamically determine the provider here
     }
      return render(request,'core/google.html',context)




def user_category_view(request):
    categories = Main_Category.objects.filter(deleted=False)  # Fetch active categories
    return render(request, 'core/user_categories.html', {'categories': categories})