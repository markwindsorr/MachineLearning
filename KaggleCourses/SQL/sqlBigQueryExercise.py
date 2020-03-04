# Exercise: Getting Started With SQL & BigQuery

"""
Intro

The first test of your new data exploration skills uses data describing crime in the city of Chicago.

Before you get started, run the following. It sets up the automated feedback system to review your answers

"""

# Set up feedack system
from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex1 import *
print("Setup Complete")

# Use the next code cell to fetch the data set

from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# (1) Count tables in the dataset. How many tables are in the Chicago Crime Dataset

#List all the tables in the "chicago_crime" dataset
tables = list(client.list_tables(dataset))
print(len(tables))
num_tables = 1

# (2) Explore the table schema. How many columns in the crime table have TIMESTAMP data?

#Construct a reference to the "crime" table
table_ref = dataset_ref.table("crime")

# API Request - fetch the table
crime_table = table_ref.get_table(table_ref)

#Print information on all the columns in the "crime" table in the "chicago_crime" datset
print(crime_table.schema)

num_timestamp_fields = 2

# (3) Create a crime map

"""
If you wanted to create a map with a dot at the location of each crime, what are the names of the two fields
you likely need to pull out of the crime table to plot the crimes on a map?
"""

# Hint: Look at the table schema. There are a couple options, but two of the fields are things commonly used to plot
# on maps. Both are 'Float' types. Use quotes around the field names in your answer

fields_for_plotting = ['latitude', 'longitude']