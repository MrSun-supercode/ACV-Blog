# Generated by Django 2.2.1 on 2019-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190506_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aboutme',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]