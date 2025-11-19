from django import forms
from.models import *

class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'
        
    
class Enrollform(forms.ModelForm):
    class Meta:
        model=enroll
        fields=['fullname','DOB','gender','mobile','address','course','timeslot']