from django.db import models


class Location(models.Model):
    lat = models.FloatField(default=None, blank=False)
    long = models.FloatField(default=None, blank=False)

    # True if location is current location of user
    user_location = models.BooleanField(default=False)
