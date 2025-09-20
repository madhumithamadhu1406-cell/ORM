from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id=models.IntegerField(primary_key=True)
    car_name=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    email=models.EmailField()
    dop=models.DateField()
class CarAdmin(admin.ModelAdmin):
    list_display=['car_id','car_name','color','email','dop']