from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contract_edit', kwargs={'pk': self.pk})