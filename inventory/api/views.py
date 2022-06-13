from rest_framework import viewsets
from inventory.api.serializer import InventorySerializers
from inventory.models import Inventory
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

# class InventoryViewSet(viewsets.ModelViewSet):
#     queryset=Inventory.objects.all()
#     serializer_class=InventorySerializers
#     authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 