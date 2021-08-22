string = input('PLease enter a string: ')

digits = 0
letters = 0

for i in string:
    if i.isdigit():
        digits += 1
    else:
        letters += 1
print(digits,letters)


#
digits = 0
letters = 0

for i in string:
    if i.isdigit():
        digits +=1
    elif i.isalpha():    #elif yazdik cunku = . / else dersek bunlari da sayar.
        letters += 1
