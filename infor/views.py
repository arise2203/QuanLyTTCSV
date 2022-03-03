from django.contrib.auth.views import LoginView
from infor.models import Truong
from django.shortcuts import render
def home_view(request):
    object_list = Truong.objects.filter()
    
    nav ='home'
    return render(request,'index.html',{
        'object_list' : object_list,
        'nav':'home',
        

    })

class SiTeloginView(LoginView):
    template_name = '../templates/login.html'