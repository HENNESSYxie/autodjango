from django.db import models
from django.contrib.auth.models import User


class Auto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mark = models.TextField(db_column='Mark')  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model')  # Field name made lowercase. This field type is a guess.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    link = models.TextField(db_column='Link')  # Field name made lowercase. This field type is a guess.
    enginecapacity = models.TextField(db_column='EngineCapacity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enginepower = models.IntegerField(db_column='EnginePower', blank=True, null=True)  # Field name made lowercase.
    fueltype = models.TextField(db_column='FuelType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transmission = models.TextField(db_column='Transmission', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drivewheels = models.TextField(db_column='DriveWheels', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    milage = models.IntegerField(db_column='Milage', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Auto'


class AdsBookmark(models.Model):
    class Meta:
        db_table = "bookmark_ads"

    user = models.IntegerField(db_column='user_id')
    ad = models.IntegerField(db_column='ad_id')
