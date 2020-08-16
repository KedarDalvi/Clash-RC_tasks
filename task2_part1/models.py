from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=14)
    email_id = models.EmailField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.email_id