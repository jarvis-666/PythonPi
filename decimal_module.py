from decimal import *
getcontext().prec = 1    # used to set the precision of the decimal numbers, default is 28
a = 0.1 + 0.2
print(a)    # this is not accurate

b = Decimal(0.1) + Decimal(0.2)     # this is a new datatype 
print(b)            # this gives precise results
b = float(b)        # if we want to convert to float data type
print(type(b))

print(0.1 + 0.2 == 0.3)     # False

print(Decimal(0.1 + 0.2))   # undesired output

print(Decimal(0.1 + 0.2) == Decimal(0.1) + Decimal(0.2))        # False

print(float(Decimal(0.1) + Decimal(0.2)) == 0.3)    # True
