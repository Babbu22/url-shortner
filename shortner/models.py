from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10)
    uuid = models.CharField(max_length=10000)
