from django.shortcuts import render
from .models import ToBookClient
from .serializers import ToBookClientSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class ToBookClientView(APIView):
    def get(self, request, *args, **kwargs):
        to_book = ToBookClient.objects.all()
        serializers = ToBookClientSerializers(to_book, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
       pass