from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SongSerializer, AlbumSerializer, MusicArtistSerializer, PlaylistSerializer
from .models import Song, Album, Music_Artist, Playlist

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.select_related('album__artist').all()
    serializer_class = SongSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', '').strip()
        if not query:
            songs = self.queryset
        else:
            songs = self.queryset.filter(
                Q(name__icontains=query) |
                Q(album__name__icontains=query) |
                Q(album__artist__name__icontains=query)
            )
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class MusicArtistViewSet(viewsets.ModelViewSet):
    queryset = Music_Artist.objects.prefetch_related('albums').all()
    serializer_class = MusicArtistSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.prefetch_related('songs').all()
    serializer_class = PlaylistSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context