# Generated by Django 5.0.7 on 2024-07-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("excelapp", "0002_remove_exceldata_name_exceldata_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exceldata",
            name="Row_ID",
            field=models.CharField(default="Berlin", max_length=255),
        ),
    ]
