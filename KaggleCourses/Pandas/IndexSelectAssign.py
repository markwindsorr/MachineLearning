#------------------------------------------------------------------------------------------------------------
# Indexing, Selecting, assigning reference

"""
You'll select specific values of a pandas DataFrame or Series too work on in most data operations, so its a 
foundational skill for data science

We'll use the Wine Reviews dataset.
"""

import pandas as pd
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup Complete")

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Look at an overview of your data by running the following line
reviews.head()

# (1) Select the description column from reviews and assign the result to the variable desc
# Hint: As an example, say we would like to select the column from a DataFrame Table.
# We have 2 options: we can call either table.column or table["column"]


desc = reviews["decription"]
# OR
desc = reviews.description

# desc is a pandas Series object, with an index matching the reviews DataFrame. In general,
# when we select one column of a table, we get a series object


# (2) Select the first value from the description column of reviews, assiging it to a variable first_description
# Hint to obtain a specific entry (corresponding to column, col and row i) in a data frame table, we can call
# table.column.iloc[i]

first_description = reviews.description.iloc[0]

# Note this is the preferred way to obtain an entry from the data frame, reviews.description[i] or 
# reviews.description.loc[i] works too

# (3) Select the first row of data(the first record) from reviews and assin it to the variable first_row
# Hint: to obtain a specific row of a DataFrame, we can use the iloc operator. 

first_row = reviews.iloc[0]

# (4) Select the first 10 values from the description column in reviews, assigning the result to variable
# first_descriptions

first_descriptions = reviews.description.iloc[:10]

# (5) Select the records with index labels 1, 2, 3, 5 and 8, assigning the result to the variable sample_reviews

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# (6) Create a variable df containing the country, province, region_1 and region_2 columns of the records with
# the index labels 0, 1, 10, 100. In other words, generate the following DataFrame:

"""
     country        province            region_1            region_2
0
1
10
100

"""

cols = ["country", "province", "region_1", "region_2"]
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# (7) Create a variable df containing the country and variety columns of the first 100 records

cols = ["country", "variety"]
df = reviews.iloc[:100, cols] 

# (8) Create a dataframe italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what

italian_wines = reviews[reviews.country == "Italy"]


# (9) Create a dataframe top_oceania_wines containing all reviews with at least 95 points out of 100 for wines from
# Australia or New Zealand


top_oceania_wines = reviews.loc[(reviews.country.isin(["Australia", "New Zealand"]))
                                                & (reviews.points >= 95)
]








