from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import InventorySerializer
from .models import Inventory
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.


class InventoryListApi(GenericAPIView):
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Inventory.objects.filter(user_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
