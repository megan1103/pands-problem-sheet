# Programming and Scripting
# Weekly Tasks 06
# Author: Megan O'Donovan

## Summary :Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

def your_sqrt(y: float) -> float: # we assign y to be a float and the function will return a float (i.e the square root of y will be a float)
    x: float = y # x is a float and will be returned at the end of the function
    for _ in range(0,7):
        x = x - (x*x-y)/(2*x) # actual function value and then dividing it by the slope
    return x

firstValue = float(input("Please enter a positive number:"))
sqrtValue = round(your_sqrt(firstValue),1)
print("The square root of {} is approx. {}.".format(firstValue,sqrtValue ))
