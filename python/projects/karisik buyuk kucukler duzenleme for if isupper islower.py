#Given 2 strings, s1, and s2 return a new
#string made of the first,
#middle and last char each input string

inputStr = "PyNaTive"
lower = []
upper = []
str_join = "".join(lower + upper)
for i in inputStr:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print(str_join)


#list oldu . ilk basta bos upper ve lower listlerini bos str olarak atasak daha mantikli olur.

lower = ""
for i in inputStr:
    if i.islower():
        lower+=i

upper = ""
for i in inputStr:
    if i.isupper():
        upper+=i

print(lower + upper)
