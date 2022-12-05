# import statements
from mysql.connector import * 
# This is used to connect the two files in the same folder
db=connect(host='localhost',port=3306,user="venkat",password="12345",database="cse_ds")

# This is used to run Sql commands in python
# This is used to run the sql commands in python like we did in marioDB
mycursor1 = db.cursor()
mycursor1.execute("desc try")
columns = []

# This is used to get the column names
for i in mycursor1:
    columns.append(i[0]) 
