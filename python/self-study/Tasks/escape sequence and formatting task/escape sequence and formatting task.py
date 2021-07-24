escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]

sentence = ("I am 40 years old.{}I have two children.{}Data Science is my IT domain.".format(escapes[0],escapes[2][1]))

print(sentence)

