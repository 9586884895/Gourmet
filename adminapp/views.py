from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from capp.models import *
from datetime import datetime
from django.core.mail import send_mail
from cook import settings


# Create your views here.
def admin_login(request):
    if request.method=='POST':
        if request.POST["username"]=="admin" and request.POST["password"]=="admin@123":
            return redirect("admin_dashboard")
        else:
            print("Error!,Login failed")
    return render(request,'admin_login.html')

def admin_dashboard(request):
    stdata=enroll.objects.all()
    s=len(stdata)
    usdata=signup.objects.all()
    u=len(usdata)
    codata=contact.objects.all()
    c=len(codata)
    rdata=notes.objects.all()
    r=len(rdata)
    return render(request,'admin_dashboard.html',{'u':u,'s':s,'c':c,'r':r,'usdata':usdata})

def admin_students(request):
    stdata=enroll.objects.all()
    return render(request,'admin_students.html',{'stdata':stdata})

def admin_contacts(request):
    codata=contact.objects.all()
    return render(request,'admin_contacts.html',{'codata':codata})

def admin_receipes(request):
    rdata=notes.objects.all()    
    return render(request,'admin_receipes.html',{'rdata':rdata})

def admin_logout(request):
    logout (request)
    return redirect('/')

def Enroll(request,id):
    enrl=get_object_or_404(enroll,id=id)
    enrl.status="Enrolled"
    enrl.update_at=datetime.now()
    enrl.save()
    # Mail sending code pending#
    sub="Enrollement Status"
    msg=f"Dear {enrl.email.fullname},\n\nCongratulations and welcome to the Gourmet Cooking Class family! 🎉\nWe’re thrilled to have you join us on this flavorful journey. Your enrollment has been successfully confirmed, and we can’t wait to start cooking up something amazing together.\n\nHere’s what happens next:\n - 📅 Your class begins on: [{enrl.update_at}]\n- 🧑‍🍳 Course Enrolled: [{enrl.course}]\n- 🕒 Time Slot: [{enrl.timeslot}]\n- 📍 Location: A-709, Wings Business Bay, Rajkot\n\nPlease arrive 10 minutes early on your first day and bring your enthusiasm (and your apron)!\n\nWarm regards,\n**Team Gourmet Cooking School**"
    from_email=settings.EMAIL_HOST_USER
    sent_mail=[enrl.email.email]
    send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=sent_mail)
    print("You Enrolled Sucessfully!")
    return redirect("admin_students")   

    

def Reject(request,id):
    enrl=get_object_or_404(enroll,id=id)
    enrl.status="Reject"
    enrl.update_at=datetime.now()
    enrl.save()
    sub="Enrollement Status"
    msg=f"Dear {enrl.email.fullname},\n\nThank you for your interest in joining the Gourmet Cooking Class.\nWe truly appreciate your enthusiasm and passion for culinary learning. Unfortunately, we were unable to confirm your enrollment at this time due to PAYMENT NOT RECEIVED.\n\nHere’s what happens next:\n\nWarm regards,\n**Team Gourmet Cooking School**"
    from_email=settings.EMAIL_HOST_USER
    sent_mail=[enrl.email.email]
    send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=sent_mail)
    print("Your admission Reject by admin!")
    # Mail sending code pending
    return redirect("admin_students")

