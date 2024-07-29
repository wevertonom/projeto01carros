from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.Place:
        instance.Place = 'Placa x '

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('pre delete')
    # print(instance.Model)

def CarInventoryUpdate():
    CarsCount = Car.objects.all().count()
    CarsValue = Car.objects.aggregate(TotalValeu=Sum('Value'))['TotalValeu']
    print( CarsCount - CarsValue)
    CarInventory.objects.create(CarsCount=CarsCount, CarsValue=CarsValue)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    CarInventoryUpdate()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    CarInventoryUpdate()