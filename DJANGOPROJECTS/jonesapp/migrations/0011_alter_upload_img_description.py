# Generated by Django 4.2.3 on 2023-07-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jonesapp', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_img',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]