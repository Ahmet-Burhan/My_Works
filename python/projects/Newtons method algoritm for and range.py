#Write a Python program that calculates a square root using Newton's Method.
x = int(input("Enter a number to calculate its square root: "))
iteration = int(input("How many iterations?: "))
#36 10 yaz
r = x

for i in range(iteration):
    r = (r + x/r) / 2

print(r)
