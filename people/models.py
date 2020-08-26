
from django.db import models


class Neighbor(models.Model):
  x_coord = models.FloatField()
  y_coord = models.FloatField()
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name