from django.db import models

class ExcelData(models.Model):
    Row_ID = models.CharField(max_length=255, default='Berlin')
    Order_ID = models.CharField(max_length=255, default='Berlin')
    Order_Date = models.DateTimeField(null=True)
    Ship_Date = models.DateTimeField(null=True)
    Ship_Mode = models.CharField(max_length=255, default='Berlin')
    Customer_ID = models.CharField(max_length=255, default='Berlin')
    Customer_Name = models.CharField(max_length=255, default='Berlin')
    Segment = models.CharField(max_length=255, default='Berlin')
    Country = models.CharField(max_length=255, default='Berlin')
    City = models.CharField(max_length=255, default='Berlin')
    State = models.CharField(max_length=255, default='Berlin')
    Postal_Code = models.CharField(max_length=255, default='Berlin')
    Region = models.CharField(max_length=255, default='Berlin')
    Product_ID = models.CharField(max_length=255, default='Berlin')
    Category = models.CharField(max_length=255, default='Berlin')
    Sub_Category = models.CharField(max_length=255, default='Berlin')
    Product_Name = models.CharField(max_length=255, default='Berlin')
    Sales = models.CharField(max_length=255, default='Berlin')
    Quantity = models.CharField(max_length=255, default='Berlin')
    Discount = models.CharField(max_length=255, default='Berlin')
    Profit = models.CharField(max_length=255, default='Berlin')
