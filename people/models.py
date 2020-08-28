
from django.db import models


class Neighbor(models.Model):
  x_coord = models.DecimalField(max_digits=5, decimal_places=2)
  y_coord = models.DecimalField(max_digits=5, decimal_places=2)
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'people/'