from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    def __str__(self):
        return self.Name
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    Model = models.CharField(max_length=200)
    Brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    FactoryYear = models.IntegerField(max_length=10)
    ModelYear = models.IntegerField(max_length=10)
    Place = models.CharField(max_length=10, blank=True, null=True) #blank e branco
    Value = models.FloatField(max_length=10)
    Photo = models.ImageField(upload_to='cars/')
    def __str__(self):
        return self.Model

class CarInventory(models.Model):
    # id = models.AutoField(primary_key=True)
    CarsCount = models.IntegerField()
    CarsValue = models.FloatField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.CarsCount} - {self.CarsValue}'