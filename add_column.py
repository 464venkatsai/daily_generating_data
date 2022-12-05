# Import Statements
import data_connector
from mysql.connector import * 
import Add_tasks

# connection established
db=connect(host='localhost',port=3306,user="venkat",password="12345",database="cse_ds")
mycur = db.cursor()

# Finding the new column which is needed to be added
for i in data_connector.columns:
    for j  in Add_tasks.values:
        if j==i:
            print(f"Column Name {j} Added Successfully")
            mycur.execute(f"alter table try add {j} char(10)")
        




