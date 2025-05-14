from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, AlbumViewSet, MusicArtistViewSet, PlaylistViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'artists', MusicArtistViewSet, basename='artist')
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls)),
]