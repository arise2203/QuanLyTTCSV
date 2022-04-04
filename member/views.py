from django.contrib.auth.views import LoginView
from infor.models import Truong
from django.shortcuts import render
def home_view(request):
    object_list = Truong.objects.filter()
    
    nav ='home'
    return render(request,'index.html',{
        'object_list' : object_list,
        'nav':'home',
        

<<<<<<< HEAD:member/views.py
# Create your views here.
=======
    })

class SiTeloginView(LoginView):
    template_name = '../templates/login.html'
>>>>>>> 58a9a7f88acb1880a89b35d5ce2ccd04ecaa1b37:infor/views.py
