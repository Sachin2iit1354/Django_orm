from django.db import models

# Create your models here.
class user_schema(models.Model):
    id=models.IntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=50)
    add=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    log_time=models.DurationField(null=True,blank=True)
    new_date=models.DurationField(null=True,blank=True)
    new_1=models.TimeField(null=True,blank=True)
    def __str__(self):
        return self.name

class Log(models.Model):
    headline = models.CharField(max_length=200)
    description = models.TextField()
    # state= models.ForeignKey('dropdown_list.State', on_delete=models.CASCADE)
    tendancy= models.CharField(max_length=200)
    heading= models.CharField(max_length=200)
    # political_party= models.ForeignKey('dropdown_list.PoliticalParty', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    log_time=models.TimeField(null=True,blank=True)
    

    def __str__(self):
        return self.news_main_headline