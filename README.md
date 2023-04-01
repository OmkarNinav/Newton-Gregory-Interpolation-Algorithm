# Newton-Gregory-Interpolation-Algorithm
Interpolation With equal interval using Newton Gregory Algorithm
Coded entirely using stock python with no imports except csv

The Data for Calculations is imported from ex1.csv  

It Also Generates a MultiDimentional Difference Table anď calculates f(x) (value to be found) using it

## Interpolation 

Interpolation is the method of estimating unknown values with the help of given set of observations. According to Theile Interpolation is, “The art of reading between the lines of the table”.
Also interpolation means insertion or filling up intermediate terms of the series. It is the technique
of obtaining the value of a function for any intermediate values of the independent variables i.e.,
of argument when the values of the function corresponding to number of values of argument are
given.

The process of computing the value of function outside the range of given values of the
variable is called extrapolation

Interpolation is based on the following assumption:
1. The values of the function should be in an increasing or decreasing order i.e., there are
no sudden change (Jumps or falls) in the values during the period of under consideration.
2. The jumps and falls in the values should be uniform, this implies that the changes in the
values of the observations should be in a uniform pattern.
3. When we apply calculus of finite differences on this, we assume that given set of observations are capable of being expressed in a polynomial form.

## Newton Gregory Forward Difference Formula (NGFDF)

Let y = f (x) be a given function of x which takes the value f(x₀), f(x₀ + h), f(x₀ + 2h)... f(x₀ + nh) for
(n + 1) equally spaced values x₀, x₀+h, x₀ + 2h,... x₀+ nh of the independent variable x.

Then 

f(x) = f(x₀) + u△f(x₀) + u(u-1)/2!△²f(x₀) + u(u-1)(u-2)/2!△³f(x₀) + ... + u(u-1)(u-2)...(u-n+1)/n!△ⁿf(x₀)

where,

u = (x - x₀)/h

## Newton Gregory Backward Difference Formula (NGBDF)

Let y = f(x) be a function of x which takes the values f(a), f(a + h), f(a + 2h), ..... f(a+ nh) for
(n + 1) equally spaced values a, a + h, ........., a + nh of the independent variable x.

Then 

f(x) = f(xₙ) + u▽f(xₙ) + u(u+1)/2!▽²f(xₙ) + u(u+1)(u+2)/2!▽³f(xₙ) + ... + u(u+1)(u+2)...(u+n-1)/n!▽ⁿf(xₙ)

where,

u = (x - xₙ)/h


here △/▽ values are obtained from Difference Table


## Difference Table

The symbol △ denotes the forward difference operator

△f(x) = f(x+h) - f(x)

In general, nth forward difference are given by

△ⁿf(x) = △ⁿ⁻¹f(x+h) - △ⁿ⁻¹f(x)

Forward Difference Table

![image](https://user-images.githubusercontent.com/127706918/229296079-1248d302-5195-467d-8f2d-27e126e665a0.png)


Similarly,

The symbol ▽ denotes the backward difference operator

▽f(x) = f(x) - f(x-h)

In general, nth backward difference are given by

▽ⁿf(x) = ▽ⁿ⁻¹f(x) - ▽ⁿ⁻¹f(x-h)

Backward Difference Table

![image](https://user-images.githubusercontent.com/127706918/229296174-99dffb88-0cf4-4050-94bd-0293138b4d89.png)
