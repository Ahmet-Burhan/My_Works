def kalan(x):
    kalansiz = []
    b = list(range(x+1))
    for x in b:
        if x%b == 0 :
            kalansiz.append(b)
        else:
            False
    




def kalansiz(sayi):
    liste = []
    for i in range(1, sayi+1):
        if sayi % i == 0:
            liste.append(i)
        return liste


print(kalansiz(10))

