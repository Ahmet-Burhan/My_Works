def organizer(**kwargs):
    ages=[]
    names=[]
    for key,value in kwargs.items():
        (ages.append(key))
        (names.append(value))
    print(names,ages, sep="\n")

print(organizer(ali=2,can=15))

