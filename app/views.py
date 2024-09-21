from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Food, FoodCategory
from app.serializers import DetailedFoodSerializer, SimpleFoodSerializer, FoodCategorySerializer


class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.all()
  serializer_class = DetailedFoodSerializer
  permission_classes = [permissions.AllowAny]


class FoodCategoryViewSet(viewsets.ModelViewSet):
  queryset = FoodCategory.objects.all()
  serializer_class = FoodCategorySerializer
  permission_classes = [permissions.AllowAny]

  @action(detail=True, methods=['get'])
  def food(self, request, pk=None):
    queryset = Food.objects.filter(category=pk)
    serializer = SimpleFoodSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)
