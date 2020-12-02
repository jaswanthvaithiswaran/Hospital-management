from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('login',views.login,name='login'),
    path('doctors',views.doctors,name='doctors'),
    path('logout',views.logout,name='logout'),
    path('addpatient',views.addpatient,name='addpatient'),
    path('patient',views.patient,name='patient')
]