from cProfile import label
from pyexpat import model
from attr import attrs, fields
# from attr import attrs
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import MyUser, Profile,Images


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields = ('student_id','full_name','school_id','date_of_birth','email','mobile_number','majors','address','job_present','status')
       

        widgets={
            'student_id':forms.TextInput(attrs={'class':'form-control'}),
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'school_id':forms.Select(attrs={'class':'form-control'}),
            'date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'}),
            'majors':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'job_present':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select'}),
            

        }
        

class UserForm(ModelForm):
    class Meta:
        model=MyUser
        fields="__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-select'}),
        }




class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields = "__all__"