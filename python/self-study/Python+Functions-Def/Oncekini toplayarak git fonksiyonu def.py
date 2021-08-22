#onceki ile sonrakini toplayarak git
#cozum 1

def accumulating_list(lst):
    k = 0
    t =[]
    for i in range(len(lst)):
        k=k+lst[i]
        t.append(k)
    return t
print(accumulating_list([1,2,3,4,5]))

#cozum 2

def accumulating(lst):
    return[sum(lst[0:i+1]) for i in range(len(lst))]
print(accumulating([1,2,3,4,5]))
