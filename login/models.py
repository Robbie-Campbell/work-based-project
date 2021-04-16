from django.db import models
from django.contrib.auth.models import User

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)