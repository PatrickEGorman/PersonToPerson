from django.db import models


class Price(models.Model):
    value = models.FloatField(default=None)

    # obo -> Or best offer
    obo = models.BooleanField(default=False)
    acceptTrade = models.BooleanField(default=False)
    item = models.ForeignKey('SaleItem')


class ItemProperty(models.Model):
    propertyName = models.TextField(default=None, blank=False)
    propertyValue = models.TextField(default='')
    item = models.ForeignKey('SaleItem')


class SaleItem(models.Model):
    title = models.TextField(default=None, blank=False)
    price = models.TextField(default='')
    description = models.TextField(default='')
