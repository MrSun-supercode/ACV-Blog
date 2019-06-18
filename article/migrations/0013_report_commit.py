# Generated by Django 2.2.1 on 2019-05-20 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0012_report_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_commit', to='article.Comment')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter_commit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
