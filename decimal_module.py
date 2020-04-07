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

print(getcontext())    # outputs the current context
# the context for arithmetic is an environment specifying precision, rounding rules, etc.

# Decimal instances can be constructed from integers, strings, floats, or tuples

print(Decimal(3.14))

# significance of a new Decimal is determined by that of input
# prec only affects when doing an arithmetic operation

# there are two ready to use contexts: BasicContext and ExtendedContext

print(BasicContext)
print(ExtendedContext)

setcontext(ExtendedContext)
print(Decimal(1) / Decimal(0))

setcontext(BasicContext)
# print(Decimal(1) / Decimal(0))    # throw a trap

# flags are set by default in BasicContext, clear them first to see the changes with every computation

setcontext(ExtendedContext)
getcontext().clear_flags()
Decimal(22) / Decimal(7)
print(getcontext())

# Decimal objects are immutable