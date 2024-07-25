from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import ExcelData
import pandas as pd
import numpy as np

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file, engine='openpyxl')
            # Process the DataFrame as needed
            # Optionally save to database
            # for index, row in df.iterrows():
            #     ExcelData.objects.create(column1=row['Column1'], column2=row['Column2'])
            
            #records = df.to_records()  # convert to records

            #for record in records:
                #purchase = ExcelData(
                    #Region=record[13],
                    #Sales=record[18],
                #)
                #purchase.save()
                
            #City = df['Region'].tolist()
            Sales1 = df.groupby(by='Region')[['Sales']].sum().reset_index()
            Region = Sales1['Region'].tolist()
            Region_Sales = Sales1['Sales'].tolist()
            
            Sales2 = df.groupby(by='Category')[['Quantity']].sum().reset_index()
            Category = Sales2['Category'].tolist()
            Category_Quantity = Sales2['Quantity'].tolist()
            
            Sales3 = df.groupby(by='Sub-Category')[['Quantity']].sum().reset_index()
            Sub_Category = Sales3['Sub-Category'].tolist()
            Sub_Category_Quantity = Sales3['Quantity'].tolist()
            
            df['Ship Date'] = pd.to_datetime(df['Ship Date'])
            
            Sales4 = df.groupby('State').agg({'Sales': 'sum', 'Profit': 'sum','Quantity': 'sum'}).reset_index()
            State = Sales4['State'].tolist()
            State_Sales = Sales4['Sales'].tolist()
            State_Profit = Sales4['Profit'].tolist()
            State_Quantity = Sales4['Quantity'].tolist()
            
            Total_Quantity1 = df['Quantity'].sum()
            Total_Quantity = np.around(Total_Quantity1,2)
            Total_Sales1 = df['Sales'].sum()
            Total_Sales = np.around(Total_Sales1,2)
            Total_Profit1 = df['Profit'].sum()
            Total_Profit = np.around(Total_Profit1,2)       

            data = {
                'Region': Region,
                'Region_Sales': Region_Sales,
                'Category' : Category,
                'Category_Quantity' : Category_Quantity,
                'Sub_Category' : Sub_Category,
                'Sub_Category_Quantity' : Sub_Category_Quantity,
                'Total_Quantity' : Total_Quantity,
                'Total_Sales' : Total_Sales,
                'Total_Profit' : Total_Profit,
                'State' : State,
                'State_Sales' : State_Sales,
                'State_Profit' : State_Profit,
                'State_Quantity' : State_Quantity
            }
            
            #data = df.to_dict(orient='split')
            return render(request, 'excelapp/display_data.html',data)
    else:
        form = UploadFileForm()
    return render(request, 'excelapp/upload.html', {'form': form})
