from django.contrib import admin
from .models import Album, Song, Playlist, Music_Artist

# Register your models here.
admin.site.register(Music_Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
