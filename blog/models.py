from django.db import models

# Create your models here.
class Blog(models.Model):
    blog=models.CharField(max_length=200)