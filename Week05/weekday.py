# Programming and Scripting
# Weekly Tasks 04
# Author: Megan O'Donovan

## Summary : Write a program that outputs whether or not today is a weekday.
## Ref: https://www.delftstack.com/howto/python/python-datetime-day-of-week/
from datetime import date
import calendar ## Calendar library is used to get the name of the day
curr_date = date.today() ## Getting the current date and name of day i.e Friday 2022-03-01
currentDay = print(calendar.day_name[curr_date.weekday()]) ## day_name() method that manages an array of the days of the week
weekEnds = ("Saturday", "Sunday")
if currentDay in weekEnds:
     print('It is the weekend, yay!')
else:
     print('Yes, unfortunately today is a weekday.')