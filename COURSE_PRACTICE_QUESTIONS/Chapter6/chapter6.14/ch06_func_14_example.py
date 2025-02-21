# Chapter 4: Functions and Libraries

#* 1. Importing a Single Function
from math import sqrt
print(sqrt(144))

#* 2. Importing a Constant
from math import pi
radius = 7
area = pi * (radius ** 2)
print(area)

#* 3. Importing Multiple Functions
from math import log, factorial, pi
print(log(1000, 10))
print(factorial(4))
print(pi)

#* 4. Importing All Functions
from math import *
print(ceil(4.2))

#* 5. Using Function Aliases
from math import remainder as rm
print(rm(30, 7))

#* 6. Module Aliases
import datetime as dt
print(dt.datetime.now())
