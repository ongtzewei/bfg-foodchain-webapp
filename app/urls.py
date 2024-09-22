from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register('categories', views.FoodCategoryViewSet)
router.register('foods', views.FoodViewSet)
router.register('notifications', views.NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf import settings
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
