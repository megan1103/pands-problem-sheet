# Programming and Scripting
# Weekly Tasks 02
# Author: Megan O'Donovan

## Summary : read in values and print calculated bmi value

weight = int(input('Enter weight(kg):'))
height = int(input('Enter height(cm):'))
# BMI is measured using kg and meters squared - height measured in cm must be changed 
newheight = (height/100)**2

# round to 2 decimal places
bmivalue = round(weight/newheight,2)

#print('The BMI is (kg/m^2) {}.' .format(bmivalue))  // This will print the bmi but the measure units won't be superscripted
print("The BMI is (kg/m\u00b2)  {}.".format(bmivalue))

