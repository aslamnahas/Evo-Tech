from django.urls import path
from .views import index ,signup , login
from . import views
app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path('signup/', signup, name="signup"),
    path('login/', views.login, name='userlogin'), 
  
]
