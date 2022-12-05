# Imports required
from data_connector import *
import pandas as pd


# This is used to run query in sql
mycursor2 = db.cursor()
mycursor2.execute("select * from try")
my_result = mycursor2.fetchall()


# inserting the values to get the data stored in the database into a excel sheet
rows = []
for j in range(0,len(my_result[1])):
    for i in range(0,len(my_result)):
        # Appends the required values
        rows.append(my_result[i][j]) 
        
        
# Making a dict for the dataframe since to avoid index
# This is to get no of rows 
added = 1
no_of_vals = int(len(rows)/len(columns))
dict_data = {}


# Inserting the key : value pair into the dict
for i in range(0,len(columns)): 
    dict_data[columns[i]]=[rows[x] for x in range((added-1)*no_of_vals,added*no_of_vals)]
    added+=1
    
         
# Making an Excel formatted data for a analysis
print(dict_data)
data_set = pd.DataFrame(dict_data)
print(data_set.head)
data_excel= data_set.to_csv("Daily_Data.csv",index=False)
