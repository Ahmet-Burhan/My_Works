#2- Yazi olarak girilen string ifadenin içindeki harfler tamamen büyük
#veya tamamen küçük ise True, küçük ve büyük harlerden oluşmuş ise False veren bir fonksiyon yazalım.

def dogru(a):
    if a != a.lower() and a.upper():
        return(False)
    else:
        return(True)


girdi = (str(input("pls write something: ")))
print(dogru(girdi))

