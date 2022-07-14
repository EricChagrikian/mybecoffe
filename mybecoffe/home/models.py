from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class PresenceTimes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    arrival = models.TimeField()
    departure = models.TimeField(null=True, blank=True)
    date = models.DateField()
    
    class Meta: 
        unique_together = ('user', 'date')