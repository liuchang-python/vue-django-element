from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    birth = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 't_user'

    def __str__(self):
        return User.username
