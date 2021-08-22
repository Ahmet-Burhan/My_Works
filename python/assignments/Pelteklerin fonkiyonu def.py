#Peltek fonksiyonu
#Solution 1
def unstretch(word):
    return word[0]+"".join([word[i] for i in range(1,len(word)) if word[i] != word[i-1]])
print(unstretch("pppoooeemmm"))

#Solution 2

def unsretch_a(word):
    return "".join([x for x,y in zip(word,word[1:]) if x!=y]) + word[-1]
print(unsretch_a("pppoooeemmm"))
