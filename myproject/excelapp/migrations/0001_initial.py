# Generated by Django 5.0.7 on 2024-07-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExcelData",
            fields=[
                ("Name", models.CharField(max_length=255)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
