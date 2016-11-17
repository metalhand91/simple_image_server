from datetime import datetime

from django.db import models

# Create your models here.


class SimpleImage(models.Model):
    title = models.CharField("Title", max_length=128, 
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    img = models.ImageField()
    datetime = models.DateTimeField("Upload datetime", auto_now_add=True)
    description = models.TextField(blank=True)
    
    def __str__(self):  
        return self.title


