from django.urls import path
from .views import home ,signup , login
from . import views
app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path('signup/', signup, name="signup"),
    path('login/', views.login, name='userlogin'), 
    path('google/',views.google, name='google'),
    path('logout/', views.custom_logout, name='logout'),
   
  
]
