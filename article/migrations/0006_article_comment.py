# Generated by Django 2.2.1 on 2019-05-10 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='articles_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
