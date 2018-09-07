import pandas as pd
import numpy as np

msft=pd.read_excel("death.xls")

print(msft.head())

# convert csv file to excel via pyhton programme

df=msft.to_excel("convertcsv.xls")

df=pd.read_excel("convertcsv.xls")

print(df.head())
