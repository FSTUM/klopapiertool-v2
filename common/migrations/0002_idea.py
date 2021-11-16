# Generated by Django 3.2.9 on 2021-11-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Idea",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("votes", models.PositiveIntegerField()),
                ("content", models.CharField(max_length=500, unique=True)),
            ],
            options={
                "ordering": ["-votes"],
            },
        ),
    ]
