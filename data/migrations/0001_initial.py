# Generated by Django 4.0.3 on 2022-03-31 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name_school', models.CharField(max_length=254)),
                ('infor_school', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='', max_length=11, null=True, verbose_name='MSSV')),
                ('full_name', models.CharField(max_length=50, verbose_name='Hoten')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date_of_birth', models.DateField(verbose_name='NgaySinh')),
                ('majors', models.CharField(max_length=254, verbose_name='Nghanh')),
                ('address', models.CharField(max_length=254, verbose_name='ĐịaChi')),
                ('mobile_number', models.IntegerField(verbose_name='Số điện thoại')),
                ('job_present', models.CharField(max_length=254, verbose_name='Côngviệc')),
                ('company', models.CharField(max_length=100, verbose_name='Côngty')),
                ('job_location', models.CharField(max_length=245)),
                ('course', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Da tot nghiep', 'Da tot nghiep'), ('Chua tot nghiep', 'Chua tot nghiep')], max_length=200, null=True, verbose_name='TrangThai')),
                ('avatar', models.ImageField(default=None, upload_to='avatar', verbose_name='Ảnh đại diện')),
                ('school_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.school')),
            ],
        ),
    ]
