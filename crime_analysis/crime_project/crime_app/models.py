from django.db import models

# Create your models here.
class district(models.Model):
    #Rank = models.IntegerField()
    Neighborhood = models.CharField(max_length=200)
    Population = models.IntegerField()
    Home_Value = models.IntegerField()
    Median_Income = models.IntegerField()
