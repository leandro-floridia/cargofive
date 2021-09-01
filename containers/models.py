from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField('date published')


class Rate(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    twenty = models.CharField(max_length=10)
    forty = models.CharField(max_length=10)
    fortyhc = models.CharField(max_length=10)
