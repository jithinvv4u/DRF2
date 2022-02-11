from rest_framework import viewsets
from inventory.api.serializer import InventorySerializers
from inventory.models import Inventory
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class InventoryViewSet(viewsets.ModelViewSet):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]