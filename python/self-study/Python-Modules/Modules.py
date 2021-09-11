from math import pi,factorial,log10
print(pi)
print(factorial(4))
print(log10(1000))



def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n-1)



