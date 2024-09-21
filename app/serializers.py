from rest_framework import serializers
from app.models import Food, FoodCategory

class FoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'url')


class FoodCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = FoodCategory
    fields = ('name', 'sort', 'url')
