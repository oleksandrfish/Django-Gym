from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from api.serializators import BarberSerializer
from treners.models import Barber

class BarberList(APIView):

    @action(methods=['get'], detail=False)
    def get(self, request, format=None):
        barbers = Barber.objects.all()
        serializer = BarberSerializer(barbers, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def post(self, request, format=None):
        serializer = BarberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarberDetail(APIView):
    def get_object(self, pk):
        try:
            return Barber.objects.get(pk=pk)
        except Barber.DoesNotExist:
            raise Http404

    @action(methods=['get'], detail=False) 
    def get(self, request, pk, format=None):
        barber = self.get_object(pk)
        serializer = BarberSerializer(barber)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=False)
    def put(self, request, pk, format=None):
        barber = self.get_object(pk)
        serializer = BarberSerializer(barber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False)
    def delete(self, request, pk, format=None):
        barber = self.get_object(pk)
        barber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
