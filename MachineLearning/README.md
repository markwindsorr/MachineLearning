<h1 align="center">
    :robot: Learning Machine Learning
</h1>

<h4 align="center">
	Traditional Approach: F(x) = Y<br>ML Approach: Input(X) + Output(Y) = F(X)
</h4>

"A computer program is said to learn from experience E with respect to some class of tasks T and a performance measure P, if its performance at tasks T, as measured by P, improves with experience E" - Tom M. Mitchell

In other words:

"An agent is learning if it improves its performance on future tasks after making observations about the world"

# Overview

## Specify Type of Problem (Supervised vs Unsupervised Learning)

Given a machine learning problem, first we need to determine if it is a supervised or unsupervised learning problem. 

### Supervised Learning

***Supervised learning*** if used when our training dataset has an attribute (a column) that contains the "answer", usually called the target or ground truth. The dataset that contains the target attribute is called "labeled" data.

### Unsupervised Learning

***Unsupervised learning*** is used when we do not have labeled data. The machine learning model is expected to learn the underlying patterns

### Semi-supervised

***Semi-supervised Learning*** is when we have some labeled data but most of it is unlabeled. We can then use a mixture of supervised and unsupervised learning techniques.


## Specify Type of Model (Supervised) Classification vs. Regression

We further have to distinguish the machine learning model as classification or regression based on what we want to output.

If the output of the machine learning model is a discrete value (non-continuous such as a boolean value), we call it a ***classification model***. (ex. Predicting whether there is a certain object in a photo)

If the output of the machine learning model is a continuous value, we call it a ***regression model***. (ex. Predicting the price of something)
____

## Machine Learning Workflow

The workflow to build a machine learning model is centralized around the data. ***Garbage In -> Garbage Out***. We ultimately want our machine learning models to be as accurate as possible when dealing with reality therefore, we need high quality data that reflects reality.


#### Raw Data 

1. Raw data comes in. We need to decide what type of problem we are looking at and what ML model to use.

#### Feature Engineering (This is a step we often come back too)

2. Once we figure out what type of problem and what model we are going to use, we then go ahead and perform ***feature engineering***. Feature engineering transform the data into its desired form. Some examples of feature engineering would include:

* Splitting the date: Separating our data into two groups (training & testing). The training dataset is used to train our model. We can then use our trained model to test on our testing dataset to see if our model works well enough to be applied to unseen data.

* Filling in missing values: We might need to "normalize" our dataset using various strategies that could include filling in missing values with the average value

* Encode: The dataset often contains non-numeric values such as categorical attributes (country, gender, city etc.). We often need to encode these string values into numerical values because if we were to use an algorithm such as linear regression, it can only deal with vectors of numbers as input

#### Training & Testing Process

3. Once we have done some feature engineering with our data & believe it is ready, we select a machine learning algorithm and start feeding the training data (Training Process). 

We now have our first model at the end of this training process. We then proceed to test our model with our testing data (Testing Process).

#### Hyper-Parameter Tuning

4. It is rarely the case that we are happy with our first trained model. One would then go back to the training process and tune some parameters that are exposed by the model that we selected. This is what we called the hyper-parameter tuning. The reason that it is highlighted as 'hyper' is because the parameters that we tune are the outermost interface that we interact with the model, which would eventually have impacts on the underlying parameters of the model. For example, for the decision tree model, one of its hyper-parameters would be the maximum height of the tree. Once set manually before the training, it would limit the number of branches and leaves that a decision tree can grow at the end, which are the underlying parameters that a decision tree model consists. 
____

## Overfitting vs Underfitting (Supervised)

* Generalization is the term that measures how well a model can predict our desired output. When was say that our model underfitting or overfitting

***Underfitting*** Our model does not fit well with the training data, meaning its function (the model) does not output values close to the training data. One reason for underfitting could be that the model is too simple to correctly capture the relationships in the data. A countermeasure would be to choose another algorithm that is better suited for the data.

***Overfitting*** Our model fits way to well to our training data, but does not generalize well to unseen data. An over-complicated model that is able to fit every piece of data would fall into the traps of noises and errors. Similarly with underfitting, you can choose another algorithm that is less complicated or you can regularize the algorithm which gives a penalty to the overly complicated algorithm steering it to generate a less compliated model while fitting the data

____

## Bias Vs. Variance

***Bias*** is the learners tendency to consistently learn the same wrong thing whereas ***Variance*** is the tendency to learn random things unrelated to the real signal.
____

Sources & Thanks To

<sub><sup>AI, A Modern Approach (Russell, Norvig)</sup></sub><br>
<sub><sup>LeetCode Machine Learning Article</sup></sub><br>
<sub><sup>A Tour of Machine Learning Algorithms - Jason Brownlee</sup></sub>