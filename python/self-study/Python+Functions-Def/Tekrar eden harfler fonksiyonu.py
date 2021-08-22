#tekrar eden hard duyarliligi
#cozum 1
def is_isogram(txt):
    txt = txt.lower()
    for letter in txt:
        if txt.count(letter) > 1:
            return False
    return True
print(is_isogram("Helo"))

#cozum 2

def isogram(txt):
    return len(txt) == len(set(txt.lower()))
print(isogram("Helo"))
