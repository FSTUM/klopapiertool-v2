# Generated by Django 3.2.9 on 2021-11-16 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="challengesecret",
            unique_together={("challenge", "secret")},
        ),
    ]