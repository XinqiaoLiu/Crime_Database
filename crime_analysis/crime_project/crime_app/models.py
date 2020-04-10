from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class district(models.Model):
    Neighborhood = models.CharField(max_length=200, primary_key=True)
    Population = models.IntegerField()
    Home_Value = models.IntegerField()
    Median_Income = models.IntegerField()
class crime(models.Model):
    ID = models.IntegerField(primary_key=True)
    #Date = models.DateField()
    Type = models.CharField(max_length=200)
    #Arrest = models.BooleanField()
    Area_id = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(77)])
