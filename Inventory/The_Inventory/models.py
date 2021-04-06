from django.db import models

# Create your models here
class Devices(models.Model):
    type = models.CharField(max_length=100, blank=True)
    Price = models.IntegerField(default = 20000)

    choices=(
        ('Available', 'Stock is available'),
        ('Sold', 'Stocks  are soldout'),
        ('Restocking', 'Restoking currently')

    )

    status = models.CharField(default='Available', max_length=200, choices=choices)
    issues = models.TextField()

    class Meta:
        abstract = True #for not displaying the table in database

    def __str__(self):
        return (f'Type:{self.type} Price:{self.Price}')


class Laptop(Devices):
    pass

class DeskTop(Devices):
    pass

class Mobile(Devices):
    pass