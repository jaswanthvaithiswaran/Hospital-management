from django.db import models
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.



class Manager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Staff must have a email")
        if not username:
            raise ValueError("Staff must have a username")
        user = self.model(
            email = email,
            username = username,
            is_doctor = is_doctor,
            is_staff = is_staff,
        )
        enc_string = pbkdf2_sha256.hash(password)
        user.set_password(enc_string)
        user.save(using=self.db)



class staff(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email',unique=True)
    username    = models.CharField(max_length=25,unique=True)
    is_doctor   = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    first_name  = models.CharField(max_length=25)
    speciality  = models.CharField(max_length=25,blank=True)
    img         = models.ImageField(upload_to='pics',blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'username'
    ]



class Patient(models.Model):
    firstname = models.CharField(max_length=20)
    lastname =models.CharField(max_length=20)
    Address = models.TextField()
    Phonenumber = models.IntegerField()
    Disease = models.TextField()
    prescribtion = models.TextField()


