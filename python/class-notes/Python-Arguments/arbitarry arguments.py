def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers :')
    print(bro1, bro2, bro3, sep='\n')

print(brothers("Tom","Ali","Can"))

bros= ["Tom","Ali","Can"]
print(brothers(*bros))

#########################################
#filter fonksiyonu kullanimi

def voweler(letter) :
    vowels = ["o", "e", "i", "u", "ı", "ü", "ö", "a"]

    if letter.lower() in vowels :
        return True
    else :
        return False

cümle = "bazen odun olmak istemişimdir."
filtered_vowels = filter(voweler , cümle)
print(list(filtered_vowels))

########################################
## Task *args
def merger(a, b, c, d):
    return f"For me, {a} {d} and {c}{b} are geniuses."


genius = ("Bill","Rossum","Guido van","Gates")
print(merger(*genius))

########################################

def gene(x = "Solomon", y = "David"):
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")




dit_gene = {"x" : "Marry", "y" : "Fred"}
print= (gene(**dit_gene))


####################

dict_couple = {"bride" : ["","",""]}



#####################

#friends = {"alfred":5 ,"thomas":10,"emily":15}

#def meaner(alfred, thomas, emily):
  #  avg = (alfred + thomas + emily)/3
 #   return("The avarage of their ages is :", avg)

#print(meaner(**friends))
    


grup = {"alfred": 44, "thomas":56, "emily" :22}
def meaner(alfred, thomas, emily):
    print("avg= ", (alfred+ thomas+ emily)/3)
         
meaner(**grup)

##################################
#Valid parantez

x = "[[{({})}]({}))"
def isValid(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""
isValid(x)






#######################################



