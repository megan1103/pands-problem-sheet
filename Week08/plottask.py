# Programming and Scripting
# Weekly Tasks 08
# Author: Megan O'Donovan

## Summary : Write a program called plottask.py that displays a 
# plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt
# Create coordinates:
x1 = np.random.randint(0,4,10)
x2 =x1**2
x3 =x1 **3

plt.plot(x1, marker = 'o', linestyle = 'dotted', color = 'green',label = 'f(x)=x')
plt.plot(x2, marker = 'o', linestyle = 'dashed', color = 'blue',label = 'g(x)=x\u00b2')
plt.plot(x3, marker = 'o', linestyle = 'solid', color = 'black',label = 'h(x)=x\u00b3')

font = {'family':'serif','color':'darkred','size':15}

plt.title("Weekly Task 8", fontdict = font)
plt.legend(loc = 'upper left')
plt.show()