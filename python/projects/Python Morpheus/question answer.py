def combination(*deger):
    total = 1
    for i in deger:
        if i < 1:
            continue   #1 de kucuk bir sayi gelince onu gec
        total *= i
    return total
print(combination(0,3, 4, 5, 6))


def snakefill(parametre):
    count = 0
    size = 1
    if parametre<1:
        return("invalid")
    while size < (parametre**2) / 2:
        count+=1
        size*=2
    return count

print(snakefill(6) )