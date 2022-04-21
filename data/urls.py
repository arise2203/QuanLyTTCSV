from unicodedata import name
from django.urls import path
from django import views

from data.views import camera, logout_profile,login_profile
from data import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('login/', views.login_profile,name='login'),
    path('logout/', views.logout_profile,name='logout'),
    path('',views.manage,name='manage'),
    # path('/',views.index,name='index'),
    path('listprofile/',views.list_profile,name='listprofile'),
    path('account/',views.account_list,name='account'),
    path('showItem/<str:pk_test>/',views.show_profile,name='show'),
    path('UpdateItem/<str:pk_test>/',views.update_profile,name='update'),
    path('addItem/', views.addProfile, name='addprofile'),
    path('addUser/', views.addUser, name='addUser'),
    path('deleteItem/<str:pk_test>/',views.delete_profile,name='delete'),
    path('deleteUser/<str:pk_test>/',views.delete_myuser,name='deleteUser'),
    # path('identify/',views.identifi,name='identify'),
    path('filter_gra/',views.filter,name='filter_gra'),
    path('filter_notGra/',views.filter_notGra,name='filternotGra'),
    
    path('editUser/<str:pk_test>/',views.update_user,name='editUser'),
    # path('video_feed',views.video_feed,name='video_feed'),
    path('upface/', views.upload,name='upface'),
    
    # path('facecam_feed', views.facecam_feed, name='facecam_feed'),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
