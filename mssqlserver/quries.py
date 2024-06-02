import pandas as pd 
from .connection import Cursor


sql_query = input("Type sql query to execute : ")
cursor = Cursor.make_cursor(sql_query)
conn = Cursor.make_connection()
data_frame = pd.read_sql_query(sql_query, conn)
print(data_frame.head())
