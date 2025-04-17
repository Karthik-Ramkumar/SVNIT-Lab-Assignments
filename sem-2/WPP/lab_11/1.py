import pandas as pd
import datetime

# a) Date time object for Jan 15 2012
a = pd.to_datetime('2012-01-15')

# b) Specific date and time of 9:20 pm
b = pd.to_datetime('2012-01-15 21:20')

# c) Local date and time
c = pd.to_datetime(datetime.datetime.now())

# d) A date without time
d = pd.to_datetime('2023-05-01').date()

# e) Current date
e = pd.Timestamp.now().date()

# f) Time from a date time
f = pd.Timestamp.now().time()

# g) Current local time
g = datetime.datetime.now().time()

print("a)", a)
print("b)", b)
print("c)", c)
print("d)", d)
print("e)", e)
print("f)", f)
print("g)", g)
