# Programming and Scripting
# Weekly Tasks 08
# Author: Megan O'Donovan

## Summary : Write a program called plottask.py that displays a 
# plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt
# Create coordinates:
x1 = np.random.randint(0,4,10) # Choose random integers between 0 and 4 in 10 steps
x2 =x1**2 # multiple x1 coordinates to the power of 2
x3 =x1 **3 # multiple x1 coordinates to the power of 3

plt.plot(x1, marker = 'o', linestyle = 'dotted', color = 'green',label = 'f(x)=x') # marker is used to highlight the points on the graph
plt.plot(x2, marker = 'o', linestyle = 'dashed', color = 'blue',label = 'g(x)=x\u00b2') # linestyle helps to distinguish between lines
plt.plot(x3, marker = 'o', linestyle = 'solid', color = 'black',label = 'h(x)=x\u00b3') # in the BMI task I learnt how to use supscripts, same method is used here in the labelling

font = {'family':'serif','color':'darkred','size':15}

plt.title("Weekly Task 8", fontdict = font)
plt.legend(loc = 'upper left')
plt.show() # regardless of lines 15-17 creating the plots, plt.show() is needed to actually show the plot
