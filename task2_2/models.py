from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.user.username
