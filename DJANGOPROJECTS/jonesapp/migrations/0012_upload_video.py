# Generated by Django 4.2.3 on 2023-07-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jonesapp', '0011_alter_upload_img_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips', models.FileField(upload_to='')),
            ],
        ),
    ]