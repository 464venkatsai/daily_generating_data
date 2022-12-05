from tkinter import *
root = Tk() 
# root.mainloop()
print()
# Real Life project
import pandas as pd
data1=[]
data2=[]
data3=[]
data1.append(True)
data2.append(True)
data3.append(True)
data_collection = {"Date":data1,"work":data2,"Hours":data3}

data_set = pd.DataFrame(data_collection)
data_excel = data_set.to_csv("data_daily.csv",index=False)  
print(data_set.head())