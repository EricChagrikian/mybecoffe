from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

# Create your models here.
class Talks(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateField(default=timezone.now, unique=True)

	def __str__(self):
		return self.title