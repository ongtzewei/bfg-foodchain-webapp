from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register('categories', views.FoodCategoryViewSet)
router.register('foods', views.FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
