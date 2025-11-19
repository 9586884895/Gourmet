from django.db import models

# Create your models here.
class signup(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class contact(models.Model):
    fullname=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()

class notes(models.Model):
    submit_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50)
    ingredient=models.TextField()
    instruction=models.TextField()
    file=models.FileField(upload_to='Receipedata')
    submit_by=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)



class enroll(models.Model):
    fullname=models.CharField(max_length=50)
    register_at=models.DateTimeField(auto_now_add=True)
    DOB=models.DateField()
    email=models.ForeignKey(signup,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    address=models.TextField()
    course=models.CharField(max_length=20)
    timeslot=models.TextField()
    enrollchoice=[
        ('Pending','Pending'),
        ('Enrolled','Enrolled'),
        ('Reject','Reject'),
    ]
    status=models.CharField(choices=enrollchoice,max_length=20)
    update_at=models.DateTimeField(blank=True,null=True)


    


