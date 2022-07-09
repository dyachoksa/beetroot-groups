# import calendar
import datetime
from calendar import TextCalendar
import sys

print("Today is", datetime.datetime.now())

text_cal = TextCalendar()

year = int(input("Please enter a year: "))
text_cal.pryear(year)

print("Size of 'text_cal' =", sys.getsizeof(text_cal))

hello = "Hello, World!"*2
print("Size of 'hello' =", sys.getsizeof(hello))
