# Generated by Django 5.0.7 on 2024-07-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("excelapp", "0004_alter_exceldata_order_date_alter_exceldata_ship_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exceldata",
            name="Order_Date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="exceldata",
            name="Ship_Date",
            field=models.DateTimeField(null=True),
        ),
    ]
