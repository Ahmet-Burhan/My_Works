x= int(input("first number: "))
y= int(input("second number: "))
z= int(input("third number: "))
if x>y>z :
    larger=x
elif y>x>z:
    larger=y
else:
    larger=z
print("Larger number is:",larger)

#if (x>y) and (x>z):
#    larger=x
#elif (y>x) and (y>z):
#    larger=y
#else:
#    larger=z
