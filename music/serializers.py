from rest_framework import serializers
from .models import Song, Album, Playlist, Music_Artist
from django.urls import reverse

class MusicArtistSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, required=False)
    albums = serializers.SerializerMethodField()

    def get_albums(self, obj):
        request = self.context.get('request')
        albums = obj.albums.all()
        return [
            {
                'id': album.id,
                'name': album.name,
                'url': request.build_absolute_uri(
                    reverse('album-detail', kwargs={'pk': album.id})
                ) if request else None,
            }
            for album in albums
        ]

    class Meta:
        model = Music_Artist
        fields = ['id', 'name', 'bio', 'image', 'albums']
        read_only_fields = ['id', 'albums']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Artist name cannot be empty.")
        return value

class AlbumSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, required=False)
    artist = MusicArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Music_Artist.objects.all(), source='artist', write_only=True
    )
    songs = serializers.SerializerMethodField()

    def get_songs(self, obj):
        request = self.context.get('request')
        songs = obj.songs.all()
        return [
            {
                'id': song.id,
                'name': song.name,
                'url': request.build_absolute_uri(
                    reverse('song-detail', kwargs={'pk': song.id})
                ) if request else None,
            }
            for song in songs
        ]

    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'artist_id', 'image', 'songs']
        read_only_fields = ['id', 'artist', 'songs']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Album name cannot be empty.")
        return value

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), source='album', write_only=True
    )
    file = serializers.FileField(allow_null=False, required=True)
    music_file = serializers.SerializerMethodField()

    def get_music_file(self, obj):
        request = self.context.get('request')
        if obj.file and hasattr(obj.file, 'url'):
            return request.build_absolute_uri(obj.file.url) if request else None
        return None

    class Meta:
        model = Song
        fields = ['id', 'name', 'album', 'album_id', 'file', 'music_file']
        read_only_fields = ['id', 'album', 'music_file']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Song name cannot be empty.")
        return value

    def validate_file(self, value):
        if not value.name.endswith(('.mp3', '.wav')):
            raise serializers.ValidationError("Only MP3 and WAV files are allowed.")
        return value

class PlaylistSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, required=False)
    songs = SongSerializer(many=True, read_only=True)
    song_ids = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), many=True, source='songs', write_only=True, required=False
    )

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'image', 'songs', 'song_ids']
        read_only_fields = ['id', 'songs']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Playlist name cannot be empty.")
        return value