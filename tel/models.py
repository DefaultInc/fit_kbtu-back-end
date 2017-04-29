from django.db import models


# Create your models here.

class Telephone(models.Model):
    user_name = models.CharField(max_length=256, null=False, blank=False, )
    phone = models.CharField(max_length=256, null=False, blank=False, )
    created_date = models.DateTimeField(auto_now_add=True, blank=False, null=False,)
