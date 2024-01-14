from django.db import models

# Create your models here.

class property(models.Model):
    p_name = models.CharField(max_length=100)
    addr = models.TextField()
    location = models.CharField(max_length=100)
    features = models.TextField()


