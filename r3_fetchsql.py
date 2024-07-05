#SQL connect to Fetch data from database
import pandas as pd

data = pd.read_csv("crop_production_india.csv")

data['Production'] = data['Production'].fillna(data['Production'].mean())



