from django.db import models

# Create your models here.
class church_finance(models.Model):
    tithes = models.IntegerField()
    offerings = models.IntegerField()
    seeds = models.IntegerField()