# 3. Current DateTime Display

# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# Import the 'datetime' module to work with date and time

import datetime
now = datetime.datetime.now()
a = now.strftime("%D")
b = now.strftime("%H:%M:%S")
print(f"Current date : {a} and time : {b}")
