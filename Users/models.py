from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf.global_settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL, MEDIA_URL

from datetime import datetime


def directory(instance, file):
    return f"{MEDIA_ROOT}/{instance.user.username or instance.student.name}/{file}"


class user(AbstractUser):

    image=models.ImageField()
    def __str__(self):
        return f'{self.username}'
    def __repr__(self):    
        return f'User - {self.username}'
    

class preferences(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    theme=models.CharField(max_length=122)
    timezone=models.CharField(max_length=255)

    

class Requests(models.Model):
    raised_by=models.ForeignKey(user, on_delete=models.CASCADE)
    content=models.TextField()
    approval=models.BooleanField(default=False, db_default=False)
    raised_date=models.DateTimeField(default=datetime.now(), db_default=datetime.now())
    # approved_by=models.ForeignKey(user, related_name= "name", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class UserBin(user):
    pass



class UserDeleteLog(user):
    pass