# Generated by Django 5.0.1 on 2025-01-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0003_alter_userpreference_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="newsImage",
            field=models.ImageField(blank=True, null=True, upload_to="news_images/"),
        ),
    ]
