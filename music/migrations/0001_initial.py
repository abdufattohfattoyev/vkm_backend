# Generated by Django 5.2.1 on 2025-05-10 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Artists',
                'db_table': 'music_artists',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music.music_artist')),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'db_table': 'music_albums',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='music/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album')),
            ],
            options={
                'verbose_name_plural': 'Songs',
                'db_table': 'music_songs',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('songs', models.ManyToManyField(blank=True, related_name='playlists', to='music.song')),
            ],
            options={
                'verbose_name_plural': 'Playlists',
                'db_table': 'music_playlists',
                'ordering': ['name'],
            },
        ),
    ]
