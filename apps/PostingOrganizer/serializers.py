from rest_framework import serializers

from apps.PostingOrganizer.models import Price
from apps.PostingOrganizer.models import ItemProperty
from apps.PostingOrganizer.models import SaleItem


class PriceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    value = serializers.FloatField()

    # obo -> Or best offer
    obo = serializers.BooleanField()
    acceptTrade = serializers.BooleanField()

    class Meta:
        model = Price
        fields = ('id',
                  'value',
                  'obo',
                  'acceptTrade')


class ItemPropertySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    propertyName = serializers.CharField()
    propertyValue = serializers.CharField()

    class Meta:
        model = ItemProperty
        fields = ('id',
                  'propertyName',
                  'propertyValue')


class SaleItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    itemProperties = ItemPropertySerializer(many=True)
    price = PriceSerializer(many=False)

    class Meta:
        model = SaleItem
        fields = ('id',
                  'title',
                  'description',
                  'itemProperties',
                  'price')
