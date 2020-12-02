from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.contrib.auth.hashers import make_password
# Create your models here.



class Manager(BaseUserManager):
    def create_user(self,username,email,password=None, **extra_fields):
        if not email:
            raise ValueError("Staff must have a email")
        if not username:
            raise ValueError("Staff should have username")
        staff = self.model(
            email = email,
            username = username,
           **extra_fields
        )
        staff.password = make_password(password)
        staff.save(using=self.db)
    def create_superuser(self,username,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_admin') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username,email, password, **extra_fields)


class staff(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email',unique=True)
    username    = models.CharField(unique=True,max_length=25)
    is_doctor   = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    first_name  = models.CharField(max_length=25)
    speciality  = models.CharField(max_length=25,blank=True)
    img         = models.ImageField(upload_to='pics',blank=True)
    objects = Manager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email'
    ]
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
   




class Patient(models.Model):
    firstname = models.CharField(max_length=20)
    lastname =models.CharField(max_length=20)
    Gender  = models.CharField(max_length=20,default="not to say")
    Phonenumber = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    Disease = models.TextField(blank=True)
    prescribtion = models.TextField(blank=True)


