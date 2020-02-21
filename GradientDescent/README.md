<h1 align="center">
    :robot: Gradient Descent
</h1>

# Overview 

Gradient descent is an optimization algorithm that is used to minimize some function. It does so by iteratively moving in the direction of the steepest descent as defined by the negative of the gradient (slope at a specific point). In ML, we can use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear/Multivariate regression and weights in neural networks. 

* First, we take out first step downhill in the direction specified by the negative gradient at our beginning point.

* Next we recalculate the negative gradient passing in the coordinates of our new point and take another step in the direction it specifies

* We continue the process iteratively until we that the bottom of our graph to a point we can no long move downhill. This is the ***local minimum***.

In summary, we are iteratively stepping downhill specified by the steepest negative gradient at each point until we have reached our local minimum which is the lowest point of our cost function.

![gradientDescent](gradientDescent1.jpeg =250x250)

## Learning Rate

Sources & Thanks To

<sub><sup>Intro to Gradient Descent & Linear Regression (Matt Nedrich)</sup></sub><br>
<sub><sup> (Matt Nedrich)</sup></sub><br>

