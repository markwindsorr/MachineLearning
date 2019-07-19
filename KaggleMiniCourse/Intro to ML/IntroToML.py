# Intro To ML on Kaggle

"""
(1) A Descision tree is a decision support tool that uses a tree like graph or model of decisions and their possible 
consequences, including change event outcomes, resources costs and utility.

A decision tree consists of three typs of nodes:

1. Decision Nodes : typically represented by squares
2. Chance Nodes : typically represendted by circles
3. End Nodes : typically represented by triangles

The predicted value from the model is at the bottom of the tree. The point at the bottom where we make the prediction
is called a leaf.

"""

"""
(2) Interpreting the data description


Mean : the average

Standard Deviation : measures how numerically spread out the values are

To interpret the min, 25%, 50%, 75%, and max values, imagne sorting each column from lowest to highest value

Min : the smallest value

25th Percentile: If you go a quarter way through the list, you'll find a number that is bigger than 25% of the values
and smaller than 75% of the values.

50th Percentile: If you go half way, you'll find a number that is bigger than 50% of the values and smaller than 50%
of the values 

75th Percentile: If you go three quarters you'll find a number that is bigger than 75% of the values and smaller than
25% of the values.

Max: The largest value 

"""


"""
(3) Selecting data for modeling

There are many ways to select a subset of your data. The pandas course covers these in more depth, but we will focus on 
two approaches for now

1. Dot notation, which we use to select the "prediction target"
2. Selecting with a column list, which we use to select the "features"

"""


"""
(4) Selecting the Prediction Target

You can pull out a variable with dot-notation. This single column is stored in a Series, which is broadly like a dataframe
with only a single column of data.

We'll use the dot notation to select the column we want to predict, which is called the prediction target. By convention, the 
prediction target is called y. 

"""

y = data.price # here we want to predict the price


"""
(5) Choosing Features

The columns that are inputted into our model (and later used to make predictions) are called "features". In my case
those would be the columns used to determine intrinsic stock price.

Sometimes, you will use all columns except the targer as features. Other times you'll be better off with fewer features

We select multiple features by providing a list of column names inside brackets. Each item in that list should be a string

By convention this data is called X

To quickly review the data we'll use to predict prices, use the describe() method and the head() method, which shows the top
few rows

Visually checking your data with these commands is an important part of a data scientists job. You'll frequently find surprises
in the dataset that deserve further inspection

"""

price_prediction_features = ["Return on Equity", "Return on Assets", "P/E", "P/B", "P/S", "Profit Margin"]

X = data[price_prediction_features]

"""
(6) Building your model

You will use scikit-learn library to create your models, one of the most popular library for modeling the types of data typically
stored in dataframes.

The steps to building and using your model are:

-Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model are specified
too

-Fit: Capture patterns from provided data. This is the heart of modeling

-Predict

-Evaluate: Determine how accurate the model's predictions are

Here is an example of defining a decision tree model with scikit-learn and fitting it with the features and target variable
"""

from sklearn.tree import DecisionTreeRegressor

#Define model. Specify a number for random_state to ensure same results each run
model = DecisionTreeRegressor(random_state=1)

#Fit model
model.fit(X, y)

"""
Many ML models allow some randomness in model training. Specifying a number for random_state ensures you get the same results
each run. This is considered good practice. You can use any number, and model quality wont depend meaningfully on exactly what 
value you choose

We now have a fitted model that we can use to make predictions

In practice, youll want to make predictions for new data rather than data we already looked at. But we'll make predictions 
for the first few rows of the training data to see how the predict function works

"""

model.predict(X.head())

"""
(7) What is Model Validation
"""
































































































