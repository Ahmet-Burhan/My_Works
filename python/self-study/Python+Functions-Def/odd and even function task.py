def slicer(*numbers):
    odds = []
    evens = []
    for i in numbers:
        if i % 2==0:
            evens.append(i)
        else:
            odds.append(i)
    print("The odd numbers are: ",odds)
    print("The even numebrs are: ",evens)

print(slicer(1,2,3,4,5,6,7))
    


