lambda x : "odd" if x % 2 !=0 else "even"
(lambda x:x[::-1])("ila")

#(avarage )

#avarage = lambda x,y: (x+y)/2
#print(avarage(3,5))



reverser = lambda x : x[::-1]
reverser(iterable)


#map()function:
kelimeler = ["qweqweqwe","asdasdasd"]
list(map(len,kelimeler))


words1 = ["you", "much", "hard"]
words2 = ["i", "you", "he"]
words3 = [ "love", "ate", "works"]
sentence = map(lambda x,y,z: x+" "+y+" "+z, words2,words3,words1)
for i in sentence:
    print(i)


#lamda filter
#filter(function,sequence) -- bool verir
first_ten = [0,1,2,3,4,5,6,7,8,9]
even = filter(lambda x:x%2==0, first_ten)
print(type(even))
print("Even numbers are: ", list(even))

#task
words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

for i in filter(lambda x: len(x)<5, words):
    print(i)

#task
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sesli=["a","e","i","o","u"]
filtered_sesli = filter(lamda x:x in vowels, first_ten) #True verenleri hafizada tutuyor
print(* filtered_sesli)#yildiz ile hafizada tutulanlari print ediyorum














    
