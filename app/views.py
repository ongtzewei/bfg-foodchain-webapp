from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from app import models
from app import serializers


class FoodViewSet(viewsets.ModelViewSet):
  queryset = models.Food.objects.all()
  serializer_class = serializers.DetailedFoodSerializer
  permission_classes = [permissions.AllowAny]

  @action(detail=True, methods=['get'])
  def replacements(self, request, pk=None):
    queryset = models.Food.objects.filter(pk=pk)
    serializer = serializers.ReplacementFoodSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)


class FoodCategoryViewSet(viewsets.ModelViewSet):
  queryset = models.FoodCategory.objects.all()
  serializer_class = serializers.FoodCategorySerializer
  permission_classes = [permissions.AllowAny]

  @action(detail=True, methods=['get'])
  def food(self, request, pk=None):
    queryset = models.Food.objects.filter(category=pk)
    serializer = serializers.SimpleFoodSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)


class NotificationViewSet(viewsets.ModelViewSet):
  queryset = models.Notification.objects.all()
  serializer_class = serializers.NotificationSerializer
  permission_classes = [permissions.AllowAny]

  def create(self, request, *args, **kwargs):
    serializer = serializer.NotificationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  