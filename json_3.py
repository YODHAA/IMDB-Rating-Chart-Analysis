import pandas as pd
import numpy as np

# first column of csv is index column
# msft=pd.read_csv("imdb.csv",index_col=0)

# print(msft.head())

# data types of each column
# leave the index column
# print(msft.dtypes)

# load specific column and print the output

#--------------------------------------------------

# make the column zero as index column
# msft =pd.read_csv("imdb.csv",index_col=0)

# here we use header to print user choice column with index as per user choice

msft=pd.read_csv("imdb.csv",header=0,usecols=['title','genre'],index_col=['title'])

print(msft)

# save the specific column to file csv
msft.to_csv("Writebackcsv.csv",index_label='Rename:COl')

df=pd.read_csv("Writebackcsv.csv")
print(df)

# print(msft.dtypes)
