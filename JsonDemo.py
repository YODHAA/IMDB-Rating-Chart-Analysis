import pandas as pd
import numpy as np

# read the csv file in excel format
msft=pd.read_csv("imdb.csv")
print(msft.head())

# convert csv to json format
df=msft.to_json("WriteJson.json")

# read this json file

df=pd.read_json("WriteJson.json")

# print the json file
print(df.head())
