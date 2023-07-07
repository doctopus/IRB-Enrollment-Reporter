
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_data = "data/enrollment.xlsx"

df_excel =pd.read_excel(excel_data, sheet_name='Sheet1')
print(df_excel)