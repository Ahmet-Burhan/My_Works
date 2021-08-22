#Given a string of odd length greater 7, return a string
#made of the middle three chars of a given String

string= input("write: ")
lenght= len(string)
lenght = lenght//2 -1


print(string[lenght:lenght+3])
