from django.urls import path,include
from .views import InventoryViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('InventoryAPI',InventoryViewSet)


urlpatterns = [
    path('',include(router.urls))
]
