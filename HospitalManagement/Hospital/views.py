from django.shortcuts import render , redirect
from .models import staff ,Patient
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,get_user_model,authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.
pid =int(0)
def Home(request):

   return render(request,"index.html")
def addpatient(request):
   if request.method=='POST':
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      gender = request.POST['gender']
      phonenumber = request.POST['phonenumber']
      email = request.POST['email']
      address = request.POST['address']
      patient = Patient(firstname=firstname,lastname=lastname,Gender=gender,Phonenumber=phonenumber,Email=email,Address=address)
      patient.save()
      messages.success(request,'user registered')
      return render(request,"AddPatient.html")
   return render(request,"AddPatient.html")

def login(request):
   if request.method== 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username,password=password)
      if user is not None:
         if user.is_admin:
            messages.error(request,'Try with admin portal')
            return render(request,"Login.html")
      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.error(request,'Invalid credentials')
         return render(request,"Login.html")

   else:
      return render(request,"Login.html")

def doctors(request):
   Doctors = staff.objects.all()
   return render(request,"Doctors.html",{'Doctors':Doctors})
def patient(request):
   if request.method=='GET':
      try:
         patientid = int(request.GET['id'])
         global pid
         pid = int(patientid)
      except:
         return render(request,"Patient.html")
      try:
         patient = Patient.objects.get(pk=patientid)
         return render(request,"Patient.html",{'patient':patient})
      except:
         messages.error(request,'patient not found')
         return render(request,"Patient.html")
      return render(request,"Patient.html",{'patient':patient})
   if request.method=='POST':
      
      disease = request.POST['disease']
      prescribtion = request.POST['prescribtion']
      print(pid)
      print(disease)
      print(prescribtion)
      try:
         patient = Patient.objects.get(pk=pid)
         patient.Disease = disease
         patient.prescribtion = prescribtion
         patient.save()
         messages.success(request,'record saved')
      except:
         messages.error(request,'patient not found')
      return render(request,"Patient.html",{'patient':patient})
   return render(request,"Patient.html")

def logout(request):
   auth.logout(request)
   return redirect('/')