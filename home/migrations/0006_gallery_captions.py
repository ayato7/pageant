# Generated by Django 3.2 on 2022-02-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_gallery_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='captions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
