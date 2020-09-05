from django.shortcuts import render
from rest_framework import mixins, viewsets


from .models import Song
from .serializers import SongSerializer


class SongViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
