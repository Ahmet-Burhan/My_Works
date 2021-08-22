#Write a function/functions that checks whether the sentence you get from the user is a palindrome.
#(Do not consider punctuation
#and special characters. Only consider "alphanumeric" characters.)

#cevap
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))



#Benim denemelerim
string = "ey edip adana'da, pide ye!"
temiz_string = string.strip("")
ters_string = temiz_string[::-1]
#print(temiz_string)

palindrome = input("Enter a sentence: ")
if palindrome == palindrome[::-1]:
    print(palindrome, "is a palindrome")
