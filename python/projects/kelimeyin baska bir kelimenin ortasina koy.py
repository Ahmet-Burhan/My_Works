#Given 2 strings, s1 and s2,
#create a new string by appending s2 in the middle of s1

s1 = "Ahmetin"
s2 = "Elmalar"

midindex = int(len(s1)/2)
new=s1[:midindex] + " " + s2 + " " + s1[midindex:]
print(new)
