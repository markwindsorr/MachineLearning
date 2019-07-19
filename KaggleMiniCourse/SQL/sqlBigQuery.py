# Introduction

"""
Structured query language is the programming language used with databasesm and it is an important skill for any 
data scientist. In this course, you will build your SQL skills using BigQuery, a web service that lets you apply
SQL to huge datasets.

"""

# (1) to use BigQuery we'll important the python package
from google.cloud import bigquery

# (2) The first step in the workflow is to create a Client object. As you'll see soon, this client object will
# play a central role in retrieving info from BigQuery Datasets
client = bigquery.Client()

"""
We'll work with a dataet of posts on Hacker News, a website focusing on CS and cybersecurity news.

In BigQuery, each dataset is contained in a corresponding project. In this case, our hacker_news dataset is contained
in the bigquery-public-data project. To access the datasetm

-We begin by constructing a reference to the dataset with the dataset() method
-Next, we use the get_dataset() method, along with the reference we just constructed, to fetch the dataset

"""

# (3) Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

#API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

"""
Every dataset is just a collection of tables. You can think of a dataset as a spreadsheet file containing multiple
tables, all composed of rows and columns

We use the list_tables() method to list the tables in the dataset

"""

#List all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

#Print names of all tables in the the data set
for table in tables:
    print(table.table_id)

"""
Table Schema

The structure of a table is called its schema. We need to understand a tables schema to effectively pull out the data
we want
"""

# Print information on all the columns in the "full" table in the "hacker_news" dataset
table.schema

"""
Each SchemaField tells us about a specific column (which we also refer to as a field). In order, the information is

-The name of the column
-The field type (data type) in the column
-The mode of the column ('Nullable' means that a column allows null values, and is the default)
-A description of the data in that column

SchemaField('by', 'string', 'NULLABLE', "The username of the item's author.",())

We can use the list_rows() method to check just the first five lines of the full table to make sure this is right
(Sometimes datbases have outdated description, so its good to check). This returns a BigQuery RowIterator object
that can quickly be converted to a pandas DataFrame with the to_dataframe() method

"""

# Preview the first five lines of the "full" table
client.list_rows(table, max_results=5).to_dataframe()

"""
The list_rows() method will also let us look at just the info in a specific column. If we want to see the first fives entries
in the by column
"""

# Preview the first five entries in the by column of the full table
client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()

