from django.contrib import admin
from django.urls import path,include
from adminapp import views




urlpatterns = [
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_students/',views.admin_students,name='admin_students'),
    path('admin_contacts/',views.admin_contacts,name='admin_contacts'),
    path('admin_receipes/',views.admin_receipes,name='admin_receipes'),
    path('admin_logout/',views.admin_logout,name='admin_logout'), 
    path('Enroll/<int:id>/',views.Enroll,name='Enroll'), 
    path('Reject/<int:id>/',views.Reject,name='Reject'),    
   
]
