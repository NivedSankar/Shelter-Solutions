from django.db import models

# Create your models here.

class property(models.Model):
    p_name = models.CharField(max_length=100)
    addr = models.TextField()
    location = models.CharField(max_length=100)
    features = models.TextField()


class Unit(models.Model):
    p_type = (
        ('1BHK', '1 Bedroom, Hall, Kitchen'),
        ('2BHK', '2 Bedrooms, Hall, Kitchen'),
        ('3BHK', '3 Bedrooms, Hall, Kitchen'),
        ('4BHK', '4 Bedrooms, Hall, Kitchen'),
    )

    img = models.FileField(upload_to='shelterapp/static/images')
    Property = models.ForeignKey(property, on_delete=models.CASCADE, related_name='units')
    type = models.CharField(max_length=10, choices=p_type)
    rent = models.IntegerField()
