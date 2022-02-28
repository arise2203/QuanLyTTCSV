from django.db import models

class Truong(models.Model):
    MaTruong = models.CharField(max_length=10, primary_key=True)
    TenTruong = models.CharField(max_length=50)


class Khoa(models.Model):
    MaKhoa= models.CharField(max_length=10,primary_key=True)
    MaTruong = models.ForeignKey(Truong, on_delete=models.CASCADE)
    TenKhoa = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100)


class Nghanh(models.Model):
    MaNghanh= models.CharField(max_length=10, primary_key=True)
    MaKhoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    TenNganh = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100, default="")


class NienKhoa(models.Model):
    MaNienKhoa= models.CharField(max_length=10, primary_key=True)
    TenNienKhoa = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100, default="")

    
class Lop(models.Model):
    MaLop = models.CharField(max_length=10,primary_key=True)
    MaNganh = models.ForeignKey(Nghanh, on_delete=models.CASCADE)
    MaNienKhoa = models.ForeignKey(NienKhoa, on_delete=models.CASCADE)
    TenLop = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=100,default="")


class TrangThai (models.Model):
    TrangThai = models.BooleanField(default=False)
    MaNienKhoa = models.ForeignKey(NienKhoa,on_delete=models.CASCADE)
    

class SinhVien(models.Model):
    MaSV =models.CharField(max_length=10,primary_key=True)
    Malop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    HoTen =models.CharField(max_length=50)
    NgaySinh = models.DateTimeField()
    GioiTinh = models.BooleanField(default=True)
    DanToc =models.CharField(max_length=50)
    DaiChi = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    NoiO = models.CharField(max_length=100)
    GhiChu = models.CharField(max_length=200,default="")

 