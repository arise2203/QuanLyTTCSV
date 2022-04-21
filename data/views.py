from itertools import count
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse
from data.models import MyUser, School, Profile,Images
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from calendar import HTMLCalendar
from .camera import FaceDetect
from .forms import ProfileForm,UserForm,ImageForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import face_recognition
from .extract_embeddings import *
from .train_model import *
import cv2
import imutils
import urllib.request
import numpy as np
import time,datetime
import data
from data import extract_embeddings,train_model,camera
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings


profile = Profile.objects.all()
schools = School.objects.all()
myuser = MyUser.objects.all()
profile_count=profile.count()







def gen(camera):
    	while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		
def facecam_feed(request):
	return StreamingHttpResponse(gen(FaceDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')
def Train(request):
    extract_embeddings.embeddings()
    train_model.model_train()
    return render(request, 'mana.html')
    cv2.destroyAllWindows()



protoPath = os.path.sep.join([ "face_detection_model\\deploy.prototxt"])
modelPath = os.path.sep.join(["face_detection_model\\res10_300x300_ssd_iter_140000.caffemodel"])
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
    #Tải model của embedding
embedder = cv2.dnn.readNetFromTorch(os.path.join('face_detection_model/openface_nn4.small2.v1.t7'))
# Tải mô hình nhận dạng cùng với bộ nhãn
recognizer = os.path.sep.join(["output\\recognizer.pickle"])
recognizer = pickle.loads(open(recognizer, "rb").read())
le = os.path.sep.join(["output\\le.pickle"])
le = pickle.loads(open(le, "rb").read())
dataset = os.path.sep.join(["dataset"])
user_list = [ f.name for f in os.scandir(dataset) if f.is_dir() ]
def detectImage(request):
    # This is an example of running face recognition on a single image
    # and drawing a box around each person that was identified.

    # Load a sample picture and learn how to recognize it.

    #upload imagerequest.method == 'POST' and
    if request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    # else:

    #     return render(request, 'home.html', context={'uploaded_file_url': uploaded_file_url})
        #person=Person.objects.create(name="Swimoz",user_id="1",address="2020 Nehosho",picture=uploaded_file_url[1:])
        #person.save()

    frame = api.load_image_file(uploaded_file_url[1:])
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    frame = imutils.resize(frame, width=600)
    (h, w) = frame.shape[:2]
    imageBlob = cv2.dnn.blobFromImage(
			cv2.resize(frame, (300, 300)), 1.0, (300, 300),
			(104.0, 177.0, 123.0), swapRB=False, crop=False)
    detector.setInput(imageBlob)
    detections = detector.forward()     
    for i in range(0, detections.shape[2]): 
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            face = frame[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]
            if fW < 20 or fH < 20:
                continue
            faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
					(96, 96), (0, 0, 0), swapRB=True, crop=False)
            embedder.setInput(faceBlob)
            vec = embedder.forward()
            preds = recognizer.predict_proba(vec)[0]
            j = np.argmax(preds)
            proba = preds[j]
            name = le.classes_[j]
            # if proba*100 <40:
                # name = "Unknown"
            text = "{}: {:.2f}%".format(name, proba * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),
					(0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            with open('attendance.csv','r+') as g:
                attendance = g.read()
                attendance = attendance.split('\n')
                if name not in attendance:
                    attendance.append(name)
                    g.close()
                    g = open('attendance.csv','w')
                    for a in attendance:
                        g.write(a)
                        g.write('\n')
                    g.close()


    cv2.imshow('frame',frame)
    cv2.waitKey(0)
    return render(request, 'mana.html')
    cv2.destroyAllWindows()




def video_feed(request):
    return StreamingHttpResponse(streamwebcam(), content_type='multipart/x-mixed-replace; boundary=frame')

def stream(request):
    def event_stream():
        while True:
            time.sleep(0.1)
            result = {
                'backend_time' : (datetime.datetime.utcnow() + datetime.timedelta(hours = 7)).strftime("%Y-%m-%d %H:%M:%S"),
                
            }
         
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def webcamera(request):
    return render(request, 'webcam.html')
def stopWebCam(request):
    return render(request, 'stopcame.html')


def upload(request):
    return render(request, 'upface.html')

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

def update_user(request,pk_test):
    school_count = schools.count()
    myuser_count=myuser.count()
    update_data = MyUser.objects.get(id=pk_test)
    form=UserForm(instance=update_data)
    if request.method =="POST":
        form=UserForm(request.POST,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect('account')

    return render(request,'./addUser.html',{
        'update_data':update_data,
        'form':form,
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
    dele_user = MyUser.objects.get(id=pk_test)
    dele_user.delete()
    messages.success(request,("Bạn đã xóa thành công"))

    return redirect('account')



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



@login_required(login_url='login')
def search_list(request):
    filter_company=Profile.objects.all().filter(company__iexact=None)
    if request.method =="POST":
        search = request.POST['search'] 
        mutiple_search = Q(Q(student_id__icontains=search) | Q(full_name__icontains =search) | Q(company__icontains=search))
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



def camera(request):
   
    return render(request, 'camera.html')


