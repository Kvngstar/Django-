from django.db import models

class upload_img(models.Model):
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='uploads/')

class upload_video(models.Model):
    clips = models.FileField(upload_to='uploads/')



