# Generated by Django 4.2.3 on 2023-07-15 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jonesapp', '0002_musician_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]
