
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
# Replace 'username', 'password', 'host', 'port', and 'database_name' with your actual database credentials
engine = create_engine('mysql+pymysql://username:password@host:port/database_name')
connection = engine.connect()
result = connection.execute('SELECT * FROM your_table')
for row in result:
    print(row)
# Close Connection
connection.close()

excel_data = "data/enrollment.xlsx"

df_excel =pd.read_excel(excel_data, sheet_name='Sheet1')
print(df_excel['MRN'])