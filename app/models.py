from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    image = models.ImageField(null=True)
    fans =  models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Picture(models.Model):
    userid = models.IntegerField()
    filename = models.ImageField()
    title = models.CharField(max_length=256)
    haveher = models.BooleanField()
    good =  models.IntegerField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

