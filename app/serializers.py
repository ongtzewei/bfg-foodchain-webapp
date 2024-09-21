from rest_framework import serializers
from app.models import Food, FoodCategory


class DetailedFoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'url')


class SimpleFoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'url')


class FoodCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = FoodCategory
    fields = ('name', 'image', 'sort', 'url')
