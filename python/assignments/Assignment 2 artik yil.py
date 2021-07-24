year = int(input("Enter a 4-digit year :"))
leap = ((year % 4 == 0)and(year % 100 !=0))or (year % 400 == 0)
print(leap)
