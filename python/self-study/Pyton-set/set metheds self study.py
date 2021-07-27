a = set()
print(type(a))

b= set("ali")
c= set("veli")
d= set("sueda")
print(b.difference(c)) #fark
print(b.union(c)) #setlerin toplami
print(b&c&d) #hepsinde kesisen bir eleman yok
print(b-c&d) #ilk once cikartma yapti ve boylece b ve c den cikanda a oldugu icin a yi ortak eleman kabul etti.
print(b.intersection(c)) #ayni elemanlar


print(d.remove('s'))
print(d.remove('u'))
print(d)

print(d.add('c'))
print(d)

print(len(b)) #direk str icindeki kelimenin harflerini aliyor

print('a' in b) #in and not in always gives True or False
print('z' not in d)


