# Generated by Django 2.2.1 on 2019-06-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]
