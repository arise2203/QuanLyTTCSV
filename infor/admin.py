from re import search
from django.contrib import admin
from .models import Truong, SinhVien, Lop,Khoa,NienKhoa,Nganh,TrangThai
# from .models import department
# Register your models here.


class TruongAdmin(admin.ModelAdmin):
    list_display = ['MaTruong','TenTruong','DiaChi']
    search_fields =['MaTruong']
    list_filter =('MaTruong','TenTruong')



class KhoaAdmin(admin.ModelAdmin):
    list_display = ['MaKhoa','TenKhoa','GhiChu']
    search_fields =['MaKhoa']
    list_filter =('TenKhoa','MaKhoa')




class NganhAdmin(admin.ModelAdmin):
    list_display = ['MaNganh','TenNganh','GhiChu']
    search_fields =['MaNganh']
    list_filter =['MaNganh','TenNganh']



class NienKhoaAdmin(admin.ModelAdmin):
    list_display = ['MaNienKhoa','TenNienKhoa','GhiChu']
    search_fields =['MaNienKhoa']
    list_filter =['MaNienKhoa']

class LopAdmin(admin.ModelAdmin):
    list_display = ['MaLop','TenLop','GhiChu']
    search_fields =['MaLop']
    list_filter =['MaLop']


class TrangThaiAdmin(admin.ModelAdmin):
    list_display = ['TrangThai','MaNienKhoa']
    search_fields =['MaNienKhoa']
    list_filter =['MaNienKhoa']


class SinhVienAdmin(admin.ModelAdmin):
    list_display = ['MaSV','HoTen','NgaySinh','Email','NoiO']
    search_fields =['MaSV']
    list_filter =['MaSV']

admin.site.register(Truong,TruongAdmin)
admin.site.register(Khoa,KhoaAdmin)
admin.site.register(Nganh,NganhAdmin)
admin.site.register(NienKhoa,NienKhoaAdmin)
admin.site.register(Lop,LopAdmin)
admin.site.register(TrangThai,TrangThaiAdmin)
admin.site.register(SinhVien,SinhVienAdmin)
