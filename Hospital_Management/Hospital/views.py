from django.shortcuts import render , redirect
from .models import staff
from django.contrib.auth.models import User, auth
# Create your views here.

def Home(request):

   return render(request,"index.html")

def login(request):
   if request.method== 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         return render(request,"Login.html")

   else:
      return render(request,"Login.html")

def doctors(request):
   Doctors = staff.objects.all()
   return render(request,"Doctors.html",{'Doctors':Doctors})