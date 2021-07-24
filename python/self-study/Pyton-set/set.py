
                                 #kumeler(sets)

set_1= {"red","blue","pink","red"}  #her defasinda cikisi farkli
colors={"red","blue","pink","red"}  #ilk once kumeye sonrada listeye degistirebilirsin set(set_1) sonra da list(set_1)
set_2= set(colors)
bosluk= ("bosluk\n\n\n")

print(set_1)
print(set_2)
print(bosluk)

letter = "a b c d e f g h i j k l m n o".split()#liste olustur
print(letter)
print(set(letter))
print(bosluk)

date = "12/07/2021"
a = set(date)
print(a)
print(len(a))
print(bosluk)

america= set("Washington")
new_zelland= set("Wellinghton")
print(america)
print(new_zelland)
print(america - new_zelland)
#print(america.diffrence(new_zelland))  bir hata var suan zamanim yok
#print(new_zelland.diffrence(america))
print(america & new_zelland)
print(america | new_zelland)
