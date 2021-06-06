from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import *
from rest_framework.views import APIView

from .permission import RegisterPermission
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class ClientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        client = Client.objects.get(user=request.user)
        serializers = ClientSerializer(client)
        return Response(serializers.data)

    def put(self, request, *args, **kwargs):
        client = Client.objects.get(user=request.user)
        serializers = ClientSerializer(client, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"Update successful!!!"})
        return Response(serializers.errors)


class WorkerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        worker = Worker.objects.get(user=request.user)
        serializers = WorkerSerializer(worker)
        return Response(serializers.data)

    def put(self, request, *args, **kwargs):
        worker = Worker.objects.get(user=request.user)
        serializers = WorkerSerializer(worker, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"Update successful!!!"})
        return Response(serializers.errors)


class RegisterModelView(ModelViewSet):
    # permission_classes = [RegisterPermission]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AuthView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
