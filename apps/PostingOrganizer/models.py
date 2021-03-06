from django.db import models


class Price(models.Model):
    value = models.FloatField(default=None)

    # obo -> Or best offer
    obo = models.BooleanField(default=False)
    acceptTrade = models.BooleanField(default=False)


class ItemProperty(models.Model):
    propertyName = models.TextField(default=None, blank=False)
    propertyValue = models.TextField(default='')
    item = models.ForeignKey('SaleItem', on_delete=models.CASCADE)


class SaleItem(models.Model):
    title = models.TextField(default=None, blank=False)
    price = models.TextField(default='')
    description = models.TextField(default='')
    price = models.OneToOneField(
        Price, on_delete=models.CASCADE
    )


class Category(models.Model):
    category_url_name = models.TextField(default=None, primary_key=True, blank=False)
    display_name = models.TextField(default=None, blank=False)
    craigslist_url_adder = models.TextField(default=None)
    type = models.TextField(default='for_sale')
