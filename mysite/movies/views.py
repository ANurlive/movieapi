from django.shortcuts import render
from .models import MovieData
from .serializer import MovieSerializer
from rest_framework import viewsets
# Create your views here.

class MovieViewSets(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSets(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSets(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer