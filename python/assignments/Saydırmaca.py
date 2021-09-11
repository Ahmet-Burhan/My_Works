string = "bugun ayriliktan bir onceki ders"
word_dict = {}
for n in string :
    
    keys = word_dict.keys()
    if  n in word_dict:
        word_dict[n] += 1
    else:
        word_dict[n] = 1

print(word_dict)

#########################
veri = ["a", "b", True, (False, 1), {"1" : 2}, [1,2], {"2" : "two"}, {2, "3"}, "c", 23, 0]
toplam = "(int","str","bool","tuple","dict","set")
toplam = {}.fromkeys(tipler,0)  #toplami dict yap.icindikileri key yap ve degerleri 0 yap.

for in in range(len(veri)):
    if type(veri[i]) == int : toplam["int"] += 1
    elif type(veri[i]) == int : toplam["str"] += 1
    elif type(veri[i]) == int : toplam["bool"] += 1
    elif type(veri[i]) == int : toplam["list"] += 1
    elif type(veri[i]) == int : toplam["set"] += 1
    elif type(veri[i]) == int : toplam["dict"] += 1
    elif type(veri[i]) == int : toplam["tuple"] += 1

print(toplam)