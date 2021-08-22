number = 0
while number <  10 :
    print (number,":", "The number is less than 10")
    number+=1
else:
    print(number,":",
          "Now number is bigger than or equal 10")


#Fill in the blanks to complete the
#program that prints all elements of the flowers list below each on separate lines such as :
            #Rose
            #Orchid
            #Tulip
    
flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers) #3
count2 = 3

while count2 > 0 :
    print(flowers[count1 - count2])
    
    count2 -= 1
    
