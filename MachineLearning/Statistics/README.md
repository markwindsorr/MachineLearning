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

* Mean: The average value

```
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

```

* Median: The mid point value

```
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)
```
* Mode: The most common value

```
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
```

### Standard Deviation

A number that describes how spread out the values are. A low SD means most values are close to the mean whereas a high SD means that the values are spread out over a wider range

### Variance

Another value that describes how spread out the values are. It is the square of the standard deviation.

### Percentiles

A measure indicating the value which a given percentage of observations falls under. So for example, given a number is the 95th percentile, 95% of 