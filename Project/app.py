#!/usr/bin/python

import pandas as pd

# Load csv
xl = pd.ExcelFile("data/raw/claims/claims-2014.xls")

# Print the sheet names
print(xl.sheet_names)
df = xl.parse(xl.sheet_names[0])

print(df.iloc[0])
print(df["Airline Name"])

print(df.groupby("Airline Name").count())

print(df.describe())
