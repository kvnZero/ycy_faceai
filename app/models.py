from django.db import models

# Create your models here.

class Picture(models.Model):
    filename = models.ImageField()
    title = models.CharField(max_length=256)
    haveher = models.BooleanField()
    good =  models.IntegerField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title