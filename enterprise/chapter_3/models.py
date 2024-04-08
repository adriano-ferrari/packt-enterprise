from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    #AbstractBaseUser,
)
from django.db.models.functions import Lower
from djmoney.models.fields import MoneyField
#from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


YESNO_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)

MAKE_CHOICES = (
    (0, '------'),
    (1, 'Buick'),
    (2, 'Cadillac'),
    (3, 'Chevrolet'),
    (4, 'Ford'),
    (5, 'GMC'),
    (6, 'Chrysler'),
    (7, 'Dodge'),
    (8, 'Jeep'),
    (9, 'Lincoln'),
    (10, 'Tesla'),
)


class VehicleModel(models.Model):
    '''
    Model Object for Database Table chapter_3_vehicle_model
    '''
    name = models.CharField(
        verbose_name = 'Model',
        max_length = 75,
        unique = True,
        blank = True,
        null = True,
    )

    class Meta:
        '''
        Meta Sub-Class for chapter_3_vehicle_model Table
        '''
        ordering = ['name',]
        verbose_name = 'Vehicle Model'
        verbose_name_plural = 'Vehicle Models'
        indexes = [
            models.Index(fields=['name']),
            #models.Index(fields=['name', 'make']),
            models.Index(fields=['-name'], name='desc_name_idx'),
            models.Index(Lower('name').desc(), name='lower_name_idx')
        ]



class Engine(models.Model):
    '''
    Model Object for Database Table chapter_3_engine
    '''
    name = models.CharField(
        verbose_name = 'Engine',
        max_length = 75,
        blank = True,
        null = True,
    )
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'model_engine',
        blank = True,
        null = True,
    )


#class engine2(models.Model):
#    '''
#    Model Object for Database Table chapter_3_practice_engine
#    '''
#    name = models.CharField(
#        verbose_name = 'Engine',
#        max_length = 75,
#        blank = True,
#        null = True,
#    )
#    vehicle_model = models.ForeignKey(
#        VehicleModel,
#        on_delete = models.CASCADE,
#        verbose_name = 'Model',
#        related_name = 'model_engine2',
#        blank = True,
#        null = True,
#    )
#
#    class Meta:
#        '''
#        Meta Sub-Class for chapter_3_practice_engine Table
#        '''
#        abstract = True
#        db_table = 'chapter_3_practice_engine'
#        ordering = ['name',]
#        verbose_name = 'Practice Engine'
#        verbose_name_plural = 'Practice Engines'
#
#
#class engine3(engine2):
#    '''
#    Model Object for Database Table chapter_3_practice_engine
#    '''
#    other_name = models.CharField(
#        verbose_name = 'Other Engine Name',
#        max_length = 75,
#        blank = True,
#        null = True,
#    )


class Vehicle(models.Model):
    '''
    Model Object for Database Table chapter_3_vehicle
    '''
    vin = models.CharField(
        verbose_name = 'VIN',
        max_length = 17,
        unique = True,
        blank = True,
        null = True,
    )
    sold = models.BooleanField(
        verbose_name = 'Sold?',
        choices = YESNO_CHOICES,
        default = False,
        blank = True,
        null = True,
    )
    price = MoneyField(
        max_digits = 19,
        decimal_places = 2,
        default_currency = 'USD',
        null = True,
        validators = [
            #MinMoneyValidator(400),
            #MaxMoneyValidator(400000),
            #MinMoneyValidator(Money(500, 'EUR')),
            #MaxMoneyValidator(Money(500000, 'EUR')),
            MinMoneyValidator({'EUR': 500, 'USD': 400}),
            MaxMoneyValidator({'EUR': 500000, 'USD': 400000}),
        ]
    )
    make = models.PositiveIntegerField(
        choices = MAKE_CHOICES,
        verbose_name = 'Vehicle Make/Brand',
        blank = True,
        null = True,
    )
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'model_vehicle',
        blank = True,
        null = True,
    )
    engine = models.ForeignKey(
        Engine,
        on_delete = models.CASCADE,
        verbose_name = 'Engine',
        related_name = 'engine_vehicle',
        blank = True,
        null = True,
    )

    def __str__(self):
        '''
        Method to return __str__ format of the Vehicle Model
        '''
        MAKE_CHOICES_DICT = dict(MAKE_CHOICES)
        return MAKE_CHOICES_DICT[self.make] + ' ' + self.vehicle_model.name

    def full_vehicle_name(self):
        '''
        Method to return full vehicle name of seller
        '''
        return self.__str__() + ' - ' + self.engine.name

    @property
    def fullname(self):
        '''
        Method to return full name of seller object as a property value
        '''
        return self.__str__() + ' - ' + self.engine.name



#class Seller(models.Model):
class Seller(AbstractUser):
    '''
    Model Object for Database Table chapter_3_seller
    '''
    name = models.CharField(
        verbose_name = 'Business Name',
        max_length = 150,
        blank = True,
        null = True,
    )
    vehicles = models.ManyToManyField(
        Vehicle,
        verbose_name = 'Vehicles',
        related_name = 'vehicle_sellers',
        related_query_name = 'vehicle_seller',
        blank = True,
    )
