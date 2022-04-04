from distutils.command.upload import upload
from unicodedata import name
from django.db import models




class School(models.Model):
    school_id = models.CharField(max_length=10,primary_key=True)
    name_school = models.CharField(max_length=254)
    infor_school = models.TextField(blank=True)


    def __str__(self):
        return self.name_school




class Profile(models.Model):
    tag=(
        ("Da tot nghiep","Da tot nghiep"),
        ("Chua tot nghiep","Chua tot nghiep"),
    )
    student_id = models.CharField('MSSV',default="",max_length=11,null=True)
    full_name= models.CharField('Hoten',max_length=50)
    email = models.EmailField('Email',max_length = 254)
    date_of_birth= models.DateField('NgaySinh')
    school_id =models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
    majors = models.CharField('Nghanh',max_length=254)
    address =models.CharField('ĐịaChi',max_length=254)
    mobile_number = models.IntegerField('Số điện thoại')
    job_present = models.CharField('Côngviệc',max_length=254)
    company = models.CharField('Côngty',max_length=100)
    job_location = models.CharField(max_length=245)
    course= models.ImageField('Ảnh đại diện',upload_to='./avatar',default=None)
    status = models.CharField('TrangThai',max_length=200,null=True,choices=tag)
    # avatar = models.ImageField('Ảnh đại diện',upload_to='./avatar',default=None)

    def __str__(self):
        return self.student_id


class MyUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField('Email', max_length=200)


    def __str__(self) -> str:
        return self.first_name + ' ' +self.last_name


class Images(models.Model):
    images=models.ImageField(upload_to='face',default=None)










