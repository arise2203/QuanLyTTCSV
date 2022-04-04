from itertools import count
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from data.models import MyUser, School, Profile,Images
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from calendar import HTMLCalendar
from .forms import ProfileForm,UserForm,ImageForm
from django.contrib.auth.decorators import login_required
import cv2
import sqlite3



profile = Profile.objects.all()
schools = School.objects.all()
myuser = MyUser.objects.all()
profile_count=profile.count()

def identifi(request):
    update_image=Images.objects.all()
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'mana.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'mana.html', {'form': form})


def filter(request):
    school_count = schools.count()
    myuser_count=myuser.count()
    filter_profile= Profile.objects.all().filter(status__iexact='Da tot nghiep')
    return render(request,'./fiter_gra.html',{
        'filter_profile':filter_profile,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
})


def filter_notGra(request):
    school_count = schools.count()
    myuser_count=myuser.count()
    filter_profile= Profile.objects.all().filter(status__iexact='Chua tot nghiep')
    return render(request,'./filter_notGra.html',{
        'filter_profile':filter_profile,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
})


def update_profile(request,pk_test):
    school_count = schools.count()
    myuser_count=myuser.count()
    update_data = Profile.objects.get(id=pk_test)
    form=ProfileForm(instance=update_data)
    if request.method =="POST":
        form=ProfileForm(request.POST,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect('listprofile')

    return render(request,'./update_profile.html',{
        'update_data':update_data,
        'form':form,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
        
    })

def addProfile(request):
    school_count = schools.count()
    myuser_count=myuser.count()
    submitted = False
    if request.method =="POST":
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listprofile')
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'./addprofile.html',{
        'submitted':submitted,
        'form':form,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
        
    })


def delete_profile(request,pk_test):
    dele_data = Profile.objects.get(id=pk_test)
    dele_data.delete()
    messages.success(request,("Bạn đã xóa thành công"))

    return redirect('listprofile')

def delete_myuser(request,pk_test):
    dele_data = MyUser.objects.get(id=pk_test)
    dele_data.delete()
    messages.success(request,("Bạn đã xóa thành công"))

    return redirect('listprofile')



def show_profile(request,pk_test):
    profiles = Profile.objects.get(id=pk_test)
    return render(request,'./show_profile.html',{
        'profiles':profiles
    })

def list_profile(request):
    profile = Profile.objects.all()
    school_count = schools.count()
    myuser_count=myuser.count()
        
    return render(request,'./list_profile.html',{
        'profile':profile,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
    })

def login_profile(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request,'LogIn success')
            login(request, user)
            
            return redirect('manage')
        else:
            messages.success(request,'LogIn Unsuccessful, please agian!!')
            return redirect('login')
        
    else:
        return render(request,'./login.html',{
            'nav':'login'

        })


def logout_profile(request):
    logout(request)
    messages.success(request,("LogOut success"))
    return redirect('manage')


def profile(request):
    profile = Profile.objects.all()
    return render(request ,'./profile',{
        
        # 'nav':'profile'
    })


def list_school(request):
    list_sclooldata= School.objects.all()
    return render(request,'./school-list.html',{
        'list_sclooldata':list_sclooldata,
        'menu':'school',
    })

@login_required(login_url='login')
def manage(request):
    school_count = schools.count()
    profile = Profile.objects.all()
    myuser_count=myuser.count()
    
    return render(request,'./mana.html',{
        'profile':profile,
        'nav':'mana',
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
        
    })



def account_list(request):
    myuser=MyUser.objects.all()
    school_count = schools.count()
    myuser_count=myuser.count()
    
    return render(request,'./account.html',{
        'myuser':myuser,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
    })


# data = Profile.objects.filter(full_name__icontains=search)
def search_list(request):
    if request.method =="POST":
        search = request.POST['search'] 
        mutiple_search = Q(Q(student_id__icontains=search) | Q(full_name__icontains =search))
        data = Profile.objects.filter(mutiple_search)
        return render(request,'./search.html',{
            'search':search,
            'data':data,
        })
    else:
        data = Profile.objects.all()



def addUser(request):
    school_count = schools.count()
    myuser_count=myuser.count()
    submitted = False
    if request.method =="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'./addUser.html',{
        'submitted':submitted,
        'form':form,
        'school_count':school_count,
        'myuser_count':myuser_count,
        'profile_count':profile_count,
        
    })

def index(request):
    return render(request,'./index.html')