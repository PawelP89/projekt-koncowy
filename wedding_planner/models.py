from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lista(models.Model):
    wearf = models.DecimalField(max_digits=8, decimal_places=2)
    wearm = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    plate_price = models.DecimalField(max_digits=8, decimal_places=2)
    music = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total(self):
        return self.wearf + self.wearm + self.quantity * self.plate_price + self.music + self.movie + self.photo
