import math

inches_str= input (' How mant inches of rain have fallen :')
inches_float= float(inches_str)
volume= (inches_float/12)*43560
gallon= volume*7.4851945
inche=int(inches_float)
print(inches_float, "in. rain on 1 acre is", gallon, "gallon")
print(inche, "in. rain on 1 acre is", gallon, "gallon")