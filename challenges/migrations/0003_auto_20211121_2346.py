# Generated by Django 3.2.9 on 2021-11-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0002_alter_challengesecret_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="description_de",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="prompt_de",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="prompt_en",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
