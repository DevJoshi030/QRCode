from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import ListTableSerializer

from .models import QRCode, Restaurant
# Create your views here.


class ListTables(APIView):

    serializer_class = ListTableSerializer

    def get(self, request, format=None):

        rest = Restaurant.objects.filter(key="123")[0]

        queryset = QRCode.objects.filter(restaurant=rest)

        data = []

        for entry in queryset:

            data.append(self.serializer_class(entry).data)

        return Response(data=data, status=status.HTTP_200_OK)
