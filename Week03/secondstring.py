# Programming and Scripting
# Weekly Tasks 03
# Author: Megan O'Donovan

## Summary :Write a program that asks a user to input a string and outputs every second letter in reverse order


firstString = input('Please enter a sentence: ')
## [::2] tells python to go every second letter and the minus sign means reverse  
print(firstString[::-2])

## If we changes -2 to -1 then the output would be the sentence but backwards
## If I wanted to remove only the first two letters in the sentence print(firstString[2::])
