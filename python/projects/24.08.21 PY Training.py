#Verilen bir kuruluşu oluşturan kelimelerin baş harflerini kullanarak kısaltma oluşturan bir fonksiyon yazınız.

def kisaltma(kurulus) :
    liste = []
    kurulus = kurulus.split()
    for i in kurulus:
        liste.append(i)


    return kurulus

    

#print(kisaltma("Turk Ticaret Odasi"))


###### ardisik sayilar

def ardışık_sayı(number) :
    number = str(number)

    number0 = number.split("1") #1 i silerek ayiriyor ve digerlerinin aliyor. 1 ler yerine bos str gosteriyor
    number1 = number.split("0") # buda 0 i siliyor
    print("ardisik sifirlarin en buyuk sayisi: ", len(max(number0))) # en fazla tekrar edenin uzunlugu
    print("ardisik burlerin en buyuk sayisi: ", len(max(number1))) # "  " "  "

print(ardışık_sayı(101010110001101))



#############

def format_number(number):
    number = str(number)
    liste = []

    while number.isdigit():
        liste.append(number[-3:])
        number = number[:-3]

    return number + ",".join(reversed(liste))

print(format_number(1000000))



