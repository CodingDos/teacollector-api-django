from django.db import models

# Create your models here.

class Tea(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name

