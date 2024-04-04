from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import NewUserForm , LoginForm


def index(request):
    return render(request, "core/index.html")


###############################################################################
       # user signup#
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
                return redirect('core/index.html')  # Redirect to your home page
    else:
        form = NewUserForm()
    return render(request, 'core/registration.html', {'form': form})


###########################################################################
        #user login#
##########################################################################

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user=authenticate(email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect('core:index')
            
    else:
       form = LoginForm()
    return render(request, 'core/userlogin.html', {'form': form})