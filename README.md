# Ex02 Django ORM Web Application
## Date: 20/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

models.py

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

```


## OUTPUT
![alt text](<Screenshot (23).png>)





## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
