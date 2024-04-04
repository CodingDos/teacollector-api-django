from django.db import models

# Create your models here.

class Tea(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    TYPE_CHOICES =[
        ('E', 'Expensive'),
        ('A', 'Average'),
        ('C', 'Cheap'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])

    def __str__(self):
        return f"{self.get_type_display()}"
    
    # class Meta:
    #     ordering = ['-date']