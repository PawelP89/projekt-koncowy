from django.db import models

# Create your models here.
class AForm(models.Model):
    wearf = models.DecimalField(max_digits=8, decimal_places=2)
    wearm = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    music = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.DecimalField(max_digits=8, decimal_places=2)

class BForm(models.Model):
    wearf = models.DecimalField(max_digits=8, decimal_places=2)
    wearm = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    music = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.DecimalField(max_digits=8, decimal_places=2)

class CForm(models.Model):
    wearf = models.DecimalField(max_digits=8, decimal_places=2)
    wearm = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    music = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.DecimalField(max_digits=8, decimal_places=2)