from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
