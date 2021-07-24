x ="www.clarusway.com"
print(x.lower()) # hepsi küçük
print(x.title()) # her kelimenin ilk harfi büyür
print(x.upper()) # hepsini büyük harf olur
print(x.capitalize()) # sadece ilk kelimenin ilk
print(x.swapcase()) # Büyükler küçük, küçükler büyük
print(x.replace("www", "https//www")) # tanımlanan değişiyor
print(x.strip()) #
print(x.replace("a", "u", 1)) # sadece bir kere
print(x.replace("a", "u")) # boş bırakılınca hepsi
print(x.replace("a", "u", 5)) # sayı fazla olsada değişmiyor.
# x = x.____ olarak koymazsak değişim olmaz.
# string .dan sonra tabtab yapınca seçenekler çıkıyor
print(x.startswith("http"))
print(x.endswith("com"))
print(x.strip("wm")) # iki taraftan gördüklerini kırptı. "w" or "m" gibi
print(x.lstrip("w")) #sol taraftan kırpar
print(x.rstrip("m")) # sağ taraftan kırpar
print(x.strip()) # space tuşlarını yok eder
