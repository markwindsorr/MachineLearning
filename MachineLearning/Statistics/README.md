<h1 align="center">
    :bar_chart: Statistics for ML
</h1>

### Data Types

To analyze data, we need to know which type of data we are working with. We can split the data types into 3 main categories:

***Numerical***

* Discrete Data - finite values (ex. Test score)
* Continuous Data - infinite values (ex. Price of an item)

***Categorical*** 

* Values that cannot be measured up against each other. Example: A color value, a car type, 

***Ordinal*** 

* Like Categorical data but can be measured up against each other. Example: School grades ... D is better than F, C is better than D, B is better than C and so on.

___

### Mean, Median & Mode

```
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
```

* Mean: The average value

```
x = numpy.mean(speed)
```

* Median: The mid point value

```
x = numpy.median(speed)
```
* Mode: The most common value

```
x = stats.mode(speed)
```

### Standard Deviation

A number that describes how spread out the values are. The square root of the variance. A low SD means most values are close to the mean whereas a high SD means that the values are spread out over a wider range

```
x = numpy.std(speed)
```

### Variance

Another value that describes how spread out the values are. It is the square of the standard deviation. a.) Find the mean b.) For each value subtract the mean and then square it c.) The variance is the average of these squared differences/.

```
x = numpy.var(speed)
```

### Percentiles

A measure indicating the value which a given percentage of observations falls under. So for example, given a number is the 95th percentile, 95% of the values fall below this one

```
x = numpy.percentile(speed, 100)
```





















