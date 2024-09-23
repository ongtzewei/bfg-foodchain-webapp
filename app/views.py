from django.conf import settings
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from twilio.rest import Client
from app import models
from app import serializers


TwiloClient = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

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
    serializer = serializers.NotificationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      NotificationViewSet.send_notification(message="Thank you! We will check in with you in a week's time to see how you're doing with your meals and progress.",
                                            mobile=serializer.validated_data['mobile'])
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  @classmethod
  def send_notification(self, message, mobile):
      try:
          message = TwiloClient.messages.create(
              from_=f"whatsapp:{settings.TWILIO_NUMBER}",
              body=message,
              to=f"whatsapp:{mobile}"
          )
      except Exception as e:
          print(e)
