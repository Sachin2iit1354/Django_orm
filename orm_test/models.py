from django.db import models

# Create your models here.
class user_schema(models.Model):
    id=models.IntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=50)
    add=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.name