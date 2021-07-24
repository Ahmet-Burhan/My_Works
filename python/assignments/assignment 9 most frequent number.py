banana = input('Please write 1 to 9 numbers and we will give you the most frequent number: ')
banana = list(banana)
en_chok_tekrar = max(banana, key=banana.count)
repeat = banana.count(en_chok_tekrar)
cevap = f"En chok tekrar eden rakam {en_chok_tekrar} ve {repeat} kere tekrar etti."
print(cevap)

  #hocanin cozumu

#numbers = [1, 3, 7, 4, 3, 0, 6, 3, 7 ,8 ,4 ,4 ,4 ,6 ,7 ,6 ,5 , 4, 12, 5, 4]
#most_frequent = max(numbers, key = numbers.count)

#print(most_frequent)

#repeat = numbers.count(most_frequent)

#result = f"The most frequent number is {most_frequent} and it was {repeat} times repeated"
#print(result)


#print(max(numbers))
#print(numbers.count(4))
