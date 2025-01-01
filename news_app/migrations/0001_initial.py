# Generated by Django 5.0.1 on 2025-01-01 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('newsID', models.AutoField(primary_key=True, serialize=False)),
                ('newsTitle', models.CharField(max_length=200)),
                ('newsBody', models.TextField()),
                ('newsClass', models.CharField(choices=[('sports', 'Sports'), ('health', 'Health'), ('politics', 'Politics'), ('economics', 'Economics'), ('technology', 'Technology')], max_length=20)),
                ('viewCounter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-viewCounter'],
            },
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_class', models.CharField(choices=[('sports', 'Sports'), ('health', 'Health'), ('politics', 'Politics'), ('economics', 'Economics'), ('technology', 'Technology')], max_length=20)),
                ('priority', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority'],
                'unique_together': {('user', 'news_class')},
            },
        ),
    ]
