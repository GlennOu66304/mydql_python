import mysql.connector as connection
import pandas as pd

try:
    mydb = connection.connect(
        host="localhost", database="app", user="root", passwd="12345678", use_pure=True
    )
    # query = "Select * from userbehavior;"
    # query = "SELECT * FROM userbehavior;"
    # result_dataFrame = pd.read_sql(query, mydb)
    # result_dataFrame.head()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM userbehavior") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mydb.close()  # close the connection
except Exception as e:
    mydb.close()
    print(str(e))
