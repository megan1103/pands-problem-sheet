# Programming and Scripting
# Weekly Tasks 02
# Author: Megan O'Donovan

## Summary : Write a program that reads in a text file and outputs the number of e's it contains.
#"r" - Read - Default value. Opens a file for reading
file = open("C:\\Users\odonovanm\Documents\csvuploader.txt", "r")

#read content of file to string
dataOriginal = file.read()

## if you want to converting all letters to lower case
#dataLower = str.lower(file.read())

#get number of occurrences of the substring in the string
letterCount = dataOriginal.count("e")

print("Number of e's in the text file :", letterCount)

