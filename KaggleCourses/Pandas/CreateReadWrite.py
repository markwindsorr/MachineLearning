
# Creating, Reading and Writing

# Set Up - Run the code cell below to load the libraries you will need (including code to check your answers)

# The checking code and notebooks used in Kaggle Learn courses

import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Set Up Complete")

# (1) Create a dataframe fruits that has 2 columns and 1 row

fruits = pd.Dataframe([[30, 21]], columns=["Apples", "Bananas"])

#Note that the data is a 2D array

# (2) Create a data frame from this diagram
"""
            Apples      Bananas
2017 Sales    35           21
2018 Sales    41           34

"""

fruit_sales = pd.Dataframe([[35, 21], [41, 34]], columns=["Apples", "Bananas"], index=["2017 Sales", "2018 Sales"])

# (3) Create a variable ingredients with a pd.Series that looks like

"""
Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object
"""

items = ["Flour", "Milk", "Eggs", "Spam"]
quantities = ["4 cups", "1 Cup", "2 Large", "1 Can"]

recipes = pd.Series(quantities, index=items, name='Dinner')

# (4) Read a csv dataset of wine review into a DataFrame called reviews

# Note that the csv files begins with an unnamed column of increasing integers. We want this to be used as the index
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# (5) Run the cell below to create and display a DataFrame called animals:

animals = pd.DataFrame({"Cows": [12,20], "Goats": [22, 19]}, index=["Year 1", "Year 2"])

# Write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv

animals.to_csv("cows_and_goats.csv")


