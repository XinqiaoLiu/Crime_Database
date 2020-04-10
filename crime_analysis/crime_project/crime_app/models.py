from django.db import models

# Create your models here.
class district(models.Model):

    Neighborhood = models.CharField(max_length=200, primary_key=True)
    Population = models.IntegerField()
    Home_Value = models.IntegerField()
    Median_Income = models.IntegerField()
