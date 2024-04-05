from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils import timezone



class Customer(AbstractUser):
    username           =   models.CharField(unique=True,null=True,blank=True,max_length=20)
    email              =   models.EmailField(unique=True)
    number             =   models.CharField(max_length=10)
    is_verified        =   models.BooleanField(default=False)
    email_token        =   models.CharField(max_length=100, null=True, blank=True)
    forgot_password    =   models.CharField(max_length=100,null=True, blank=True)
    last_login_time    =   models.DateTimeField(null = True, blank = True)
    last_logout_time   =   models.DateTimeField(null=True,blank=True)
    referral_code      =   models.CharField(max_length=100,null=True, unique=True)
    referral_amount    =   models.IntegerField(default=0)
    date_joined = models.DateTimeField(default=timezone.now)  # New field for registration date

    wallet_bal         =   models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    
Customer._meta.get_field('groups').remote_field.related_name = 'customer_groups'
Customer._meta.get_field('user_permissions').remote_field.related_name = 'customer_user_permissions'




# #category


# class Main_Category(models.Model):
#     name = models.CharField(max_length=100)
#     descriptions = models.TextField(default='Default Description')
#     offer = models.PositiveIntegerField(default=0, null=True, blank=True)
#     img = models.ImageField(upload_to='categories', default='null', null=True, blank=True)
#     deleted = models.BooleanField(default=False)
#     objects = models.Manager()

#     def __str__(self):
#         return str(self.name)
