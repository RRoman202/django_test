# Generated by Django 4.2.1 on 2023-06-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_playlist_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
