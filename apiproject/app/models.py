from django.db import models
from django.conf import settings

class employee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name

class register(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    emp_id = models.IntegerField()