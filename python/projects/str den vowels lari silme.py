#Program to remove vowels from a String
# List all the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

string = input("write something: ").lower()
for i in vowels:
    string = string.replace(i, "")

print("Here: ",string)


