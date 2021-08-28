import random            # FOR LOOP VE LIST COMPRESSION ARASINDA KI HIZ FARKI
from timeit import timeit

def for_loop():
    result = []

    for i in range(1000000):
        result.append(i)
    return result

def list_comprehension():
    return[i for i in range(1000000)] 

#print(timeit(for_loop, number=1000)) #arkada calisiyor fark etmiyon
#print(timeit(for_loop, number=1))


#simdi sureleri hesaplayalim

time1 = timeit(for_loop, number=1000)
time2 = timeit(list_comprehension, number=1000)
print(f"List compression is {round(time1/time2,2)} times faster than for loop") #yuzde 2.68 for loop dan hizli #falan filan
