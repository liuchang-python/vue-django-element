from django.db import models


# Create your models here.

class Student(models.Model):
    gender_choices = (
        (0,'male'),
        (1,'female'),
        (2,'other'),
    )

    name = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    gender = models.SmallIntegerField(choices=gender_choices,default=0)
    phone = models.CharField(max_length=11)
    pic = models.ImageField(upload_to='pic',default='pic/1.jpg')


    @property
    def stu_pic(self):
        return '%s%s%s' % ('http://127.0.0.1:8000/', 'media/', self.pic)

    class Meta:
        db_table = 't_student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
