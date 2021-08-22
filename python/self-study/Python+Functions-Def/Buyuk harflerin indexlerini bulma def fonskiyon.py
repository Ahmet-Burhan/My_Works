
#Result 1
def index_of_caps(word):
    result = []
    for letter in word:
        if letter.isupper():
            result.append(word.index(letter))
    return result
print(index_of_caps("EdAbJ"))

#Result 2
def index_upper(word):
    return[word.index(letter) for letter in word if letter.isupper()]
print(index_upper("EdAbJ"))
