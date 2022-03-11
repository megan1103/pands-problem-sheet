# Programming and Scripting
# Weekly Tasks 04
# Author: Megan O'Donovan

## Summary : Collatz conjecture says that if you start with any positive integer, you’ll always end up in a loop 4, 2 and 1.
#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.



n = int(input('Please enter a positive number: '))

# Creating a list, starting with the value n and then all values computed in the loop will follow
terms = [n, ]

# The example can't start with 1, it has to be a positive number
while n != 1:
    if n % 2 == 0: ## If n is even then divide by 2
        n = n / 2
        terms.append(int(n)) # Since we want all the values in the loop to show; append() method in python adds a single item to the existing list
    else: # if n isn't even then it's odd and we apply 3n+1
        n = 3 * n + 1
        terms.append(int(n))
print(terms)