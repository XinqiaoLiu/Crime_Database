from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.conf import settings
from datetime import datetime

# Create your models here.
class district(models.Model):
    Neighborhood = models.CharField(max_length=200, primary_key=True)
    Population = models.IntegerField()
    Home_Value = models.IntegerField()
    Median_Income = models.IntegerField()
class crime(models.Model):
    ID = models.IntegerField(primary_key=True)
    Ctime = models.DateTimeField(default=datetime.now)
    Type = models.CharField(max_length=200)
    #Arrest = models.BooleanField()
    Area_id = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(90)])
class district_id(models.Model):
    ID = models.IntegerField(primary_key=True)
    Neighborhood = models.CharField(max_length=200)
class danger(models.Model):
    Type = models.CharField(max_length=500)
    Gender = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Level = models.FloatField()
    class Meta:
        unique_together = (("Type","Gender","Age"),)
