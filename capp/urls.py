from django.contrib import admin
from django.urls import path,include
from capp import views

urlpatterns = [
    path('',views.index),
    path('chefs/',views.chefs,name='chefs'),
    path('mycontact/',views.mycontact,name='mycontact'),
    path('courses/',views.courses,name='courses'),
    path('recipes/',views.recipes,name='recipes'),
    path('login/',views.login,name='login'),
    path('usignup/',views.usignup,name='usignup'),
    path('profile/',views.profile,name='profile'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('vegan/',views.vegan,name='vegan'),
    path('grill/',views.grill,name='grill'),
    path('desert/',views.desert,name='desert'),
    path('school/',views.school,name='school'),
    path('training/',views.training,name='training'),
    path('enrollform/',views.enrollform,name='enrollform'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('note/',views.note,name='note'),
    path('receipeoth/',views.receipeoth,name='receipeoth'),
    path('r1/',views.r1,name='r1'),
    path('r2/',views.r2,name='r2'),
    path('r3/',views.r3,name='r3'),
    path('r4/',views.r4,name='r4'),
    path('r5/',views.r5,name='r5'),
    path('r6/',views.r6,name='r6'),
    path('r7/',views.r7,name='r7'),
    path('r8/',views.r8,name='r8'),
    path('r9/',views.r9,name='r9'),
]
