##bir hata var bulamadim


import random
chr(68)
print(random.randint(65,90))
print(chr(68))
print(chr(random.randint(65,90)))


###  password hacker ###

uppers = [chr(random.randint(65,90)) for i in range(3)]   #random 65 90 arasinda 3 sayi belirliyor ve bulari ascii koduna ceviriyor
print("".join(uppers))  #join ile liste elemanlari birbirine yapistiriyor

lowers = [chr(random.randint(97,122)) for i in range(3)]  #yukaridakinin kucuk harf olani

numbers = [chr(random.randint(48,50)) for i in range(3)]  #numara olani

characters = chr(random.randint(33,47)) + chr(random.randint(58,64))   #noktalama isaretleri vs.

password = "".join(uppers) +"".join( lowers) + "".join(numbers) + "".join(characters)
#print(password)   # simdi birlesik rastgele bir parola elde ettik.simdi bu degistirelim


#print(random.shuffle(uppers))
#bir fonksiyon yapalim
 def shuffleit(cancan) :
     templist = list(cancan)
     random.shuffle(cancan)
     return "".join(templist)

password_2 = shuffleit("""PWPgne012"<""")
print(password_2) 