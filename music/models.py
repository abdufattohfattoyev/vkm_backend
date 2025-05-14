from django.db import models


class Music_Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Artists'
        db_table = 'music_artists'


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Music_Artist, on_delete=models.CASCADE, related_name='albums')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Albums'
        db_table = 'music_albums'


class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    file = models.FileField(upload_to='music/', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Songs'
        db_table = 'music_songs'


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Playlists'
        db_table = 'music_playlists'
