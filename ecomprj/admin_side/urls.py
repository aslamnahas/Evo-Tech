from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/',views.users,name='users'),
    path('categories/',views.main_category,name='categories'),
    path('add_main_category/',views.add_main_category,name='add_main_category'),
    # Other URL patterns
]
