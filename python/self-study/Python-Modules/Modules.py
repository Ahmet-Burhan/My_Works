from math import pi,factorial,log10
import math
import string as stg
import datetime
import random
from random import choice



print(pi)
print(factorial(4))
print(log10(1000))



def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n-1)

def factor_2(x):

    result = 1
    for i in range(x):
        result *= (i+1)
    return print(result)

print(factor(3))

print(dir(math))

print(stg.punctuation)
print(stg.digits)
print(".............................................")

print(datetime.date.today())
print(datetime.datetime.now())

number = [1,2,3,4,5,6,7,8,9,10]
print(choice(number))

print(random.random())

print(dir(random))


def fuc(y):
    return print(y)

fuc("burhan")
