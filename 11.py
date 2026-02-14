# 12. Monthly Calendar Display

# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module

import calendar
y = int(input("Enter the year : "))
m = int(input("Enter the month : "))
calendar_ = calendar.month(y, m)
print(calendar_)