#Write a Python code that displays the unique vowels found in a word entered by the user.
# List all the vowels



vowels = ['a', 'e', 'i', 'o', 'u']


   #SOLUTION 1
        
    
string = input("Provide a string to search vowels: ")
found = []
#Iterate string
for letter in string:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
        
    
    #SOLUTION 2
found = set()
for letter in string:
    if letter in vowels:
        found.add(letter)
print(found)
