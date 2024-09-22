from rest_framework import serializers
from app.models import Food, FoodCategory, Notification


class SimpleFoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'url')


class DetailedFoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'calories', 'carbohydrates', 'fat_total', 'protein', 'sodium', 'iron', 'calcium', 'url')


class ReplacementFoodSerializer(serializers.HyperlinkedModelSerializer):
  replacements = SimpleFoodSerializer(many=True, read_only=True)
  class Meta:
    model = Food
    fields = ('id', 'name', 'image', 'replacements')


class FoodCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = FoodCategory
    fields = ('name', 'image', 'sort', 'url')


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Notification
    fields = ('message', 'is_pushed', 'url')