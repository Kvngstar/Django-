# Generated by Django 4.2.3 on 2023-07-15 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jonesapp', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]