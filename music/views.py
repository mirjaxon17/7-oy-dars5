from django.shortcuts import render
from music.models import Artist, Album, Song
from music.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ArtisAPIViewSet(viewsets.ModelViewSet):
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AlbumAPIViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class SongAPIViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


