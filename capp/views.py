from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import *
from .models import *
import random
from cook import settings
from django.core.mail import send_mail
from .models import notes

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,"index.html",{'user':user})

otp=0
def login(request):
    msg=""
    global otp
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['password']               
        user=signup.objects.filter(email=email,password=pas)        

        if user: # condition true          
            # otp Sending code
            otp=random.randint(111111,999999)
            sub="One Time Password"
            msg=f"Dear User,\n\nYour One-Time Password (OTP) for verification is:\n\n🔐 OTP:{otp}\n\nIf you didn’t request this, please ignore this message.\n\nWarm regards,\n**Team Gourmet Cooking School**"
            from_email=settings.EMAIL_HOST_USER
            sent_mail=[email]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=sent_mail)
            request.session["user"]=email
            return redirect('otpverify')
                   
        else:
            print("login Error!")
            msg="Login Error, Please try agian"
    return render(request,"login.html",{'msg':msg})

def usignup(request):
    msg=""
    if request.method=="POST":
        form=signupform(request.POST)
        em=request.POST["email"]
        email=signup.objects.filter(email=em).exists()
        if email:
            print("Email id already Exists")
            msg="Email address already Exists"
        else:
            if form.is_valid():
                form.save()
                msg="Signup-Sucessfully"
                print(msg)
                return redirect('login')
            else:
                print(form.errors)
                msg="Error ! Something went Wrong..."
    return render(request,"signup.html",{'msg':msg})

def chefs(request): # chefs= About-us chef.html=Aboutus
    user=request.session.get("user")
    return render(request,"chefs.html",{'user':user})

def mycontact(request):
    user=request.session.get("user")
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            print("Msg Sent Sucessfully")
            return redirect('mycontact')
        else:
            print(form.errors)
    return render(request,"contacts.html",{'user':user})

def courses(request):
    user=request.session.get("user")
    return render(request,"courses.html",{'user':user})

def recipes(request):
    user=request.session.get("user")
    return render(request,"recipes.html",{'user':user})

def vegan(request):
    return render(request,"vegan.html")
def r1(request):
    return render(request,"r1.html")
def r2(request):
    return render(request,"r2.html")
def r3(request):
    return render(request,"r3.html")

def grill(request):
    return render(request,"grill.html")
def r4(request):
    return render(request,"r4.html")
def r5(request):
    return render(request,"r5.html")
def r6(request):
    return render(request,"r6.html")

def desert(request):
    return render(request,"desert.html")
def r7(request):
    return render(request,"r7.html")
def r8(request):
    return render(request,"r8.html")
def r9(request):
    return render(request,"r9.html")

def school(request):
    return render(request,"school.html")
def training(request):
    return render(request,"training.html")

def profile(request):
    msg=""
    em=request.session.get("user")
    cuser=signup.objects.get(email=em)
    if request.method=="POST":
        form=signupform(request.POST,instance=cuser)
        if form.is_valid():
            form.save()
            msg="update sucessfully!"
            return redirect('/')
        else:
            print(form.errors)
    return render(request,"profile.html",{'em':cuser})

def userlogout(request):
    logout(request)
    return redirect('/')

def receipeoth(request):
    ndata=notes.objects.all()
    return render(request,"receipeoth.html",{'ndata':ndata})  
    
    


def otpverify(request):
    global otp
    print(otp)
    if request.method=='POST':
        myotp=request.POST['otp']
        if otp==int(myotp):
            print("Login sucessfully")
            user=request.session.get("user")
            return redirect('/')        
        else:
            print("Error ! Please try again")
    return render(request,'otpverify.html')

def enrollform(request):
    user=request.session.get("user") 
    if not user:
        return redirect('login')   
    try:        
        email=signup.objects.get(email=user)       
        if request.method=="POST":
            form=Enrollform(request.POST)
            if form.is_valid():
                temp=form.save(commit=False)
                temp.status="Pending"
                temp.email=email
                temp.save()
                print("Your Enrollment form sucessfully submitted")
                return redirect('/')
            else:
                print(form.errors)
    except: 
        print("Errors!")
    return render(request,"enroll.html",{'user':user})

def note(request):
    msg=""
    em=request.session.get("user")
    cuser=signup.objects.get(email=em)
    #email=request.POST['email']
    #name=request.POST['submit_by'] 
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['submit_by']                         
        form=notesform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            sub="Receipe Submission Status"
            msg=f"Dear {name},\n\nYour Receipe Submission Sucessfully Done on Our Platform.\n\nWe heartly thanks to you for sharing your intrest in Receipe sharing.\n\n Your Receipe is Very useful For our Visitors.\n\nWarm regards,\n**Team Gourmet Cooking School**"
            from_email=settings.EMAIL_HOST_USER
            sent_mail=[email]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=sent_mail)
            msg="Receipe Submit-Sucessfully"
            print(msg)
            return redirect('/')
        else:
            print(form.errors)
            msg="Error ! Something went Wrong..."
    return render(request,"notes.html",{'em':cuser})



    



