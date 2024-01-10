from django.db import models

class Bean(models.Model):
  name = models.CharField(max_length=30)
  origin = models.CharField(max_length=40)
  description = models.TextField(max_length=250)
  cooking_time = models.CharField(max_length=50)
  image = models.TextField(max_length=250)
  common_uses = models.TextField(max_length=250)
  nutritional_info = models.TextField(max_length=250)
