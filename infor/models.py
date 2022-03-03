from email.policy import default
from json import load
from django.db import models

class Truong(models.Model):
    MaTruong = models.CharField(max_length=10, primary_key=True)
    TenTruong = models.CharField(max_length=50)
    # LogoTruong = models.ImageField(upload_to='images',default="")
    Gioithieu = models.CharField(max_length=1000,default="")
    DiaChi = models.CharField(max_length=100,default="")

    def __str__(self):
        return f"{self.MaTruong},{self.TenTruong},{self.Gioithieu},{self.DiaChi}"


class Khoa(models.Model):
    MaKhoa= models.CharField(max_length=10,primary_key=True)
    MaTruong = models.ForeignKey(Truong, on_delete=models.CASCADE)
    TenKhoa = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100,default="")

    
    def __str__(self):
        return f"{self.MaKhoa},{self.MaTruong},{self.TenKhoa},{self.GhiChu}"


class Nganh(models.Model):
    MaNganh= models.CharField(max_length=10, primary_key=True)
    MaKhoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    TenNganh = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.MaNganh},{self.MaKhoa},{self.TenNganh},{self.GhiChu}"


class NienKhoa(models.Model):
    MaNienKhoa= models.CharField(max_length=10, primary_key=True)
    TenNienKhoa = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.MaNienKhoa},{self.TenNienKhoa},{self.GhiChu}"

    
class Lop(models.Model):
    MaLop = models.CharField(max_length=10,primary_key=True)
    MaNganh = models.ForeignKey(Nganh, on_delete=models.CASCADE)
    MaNienKhoa = models.ForeignKey(NienKhoa, on_delete=models.CASCADE)
    TenLop = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100,default="")

    def __str__(self):
        return f"{self.MaLop},{self.MaNganh},{self.MaNienKhoa},{self.TenLop},{self.GhiChu}"



class SinhVien(models.Model):
    MaSV =models.CharField(max_length=10,primary_key=True)
    Malop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    HoTen =models.CharField(max_length=50)
    NgaySinh = models.DateField()
    GioiTinh = models.CharField(default='Nam',max_length=10)
    DanToc =models.CharField(max_length=50)
    DaiChi = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    NoiO = models.CharField(max_length=100)
    GhiChu = models.CharField(max_length=200,default="")


    def __str__(self):
        return f"{self.MaSV},{self.HoTen},{self.NgaySinh},{self.GioiTinh},{self.DanToc},{self.DaiChi},{self.Email},{self.NoiO},{self.GhiChu}"

class avata(models.Model):
    MaSV = models.ForeignKey(SinhVien,on_delete=models.CASCADE)
    imge = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.MaSV},{self.imge}"

class TrangThai (models.Model):
    MaSV = models.ForeignKey(SinhVien,on_delete=models.CASCADE,primary_key=True,default="",unique=True)
    MaNienKhoa = models.ForeignKey(NienKhoa,on_delete=models.CASCADE)
    TrangThai = models.CharField(default="Chưa ra trương", max_length=100)
    
    def __str__(self):
        return f"{self.TrangThai},{self.MaNienKhoa}"
