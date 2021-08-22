n = int(input("Enter a number: "))
count = 0

for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or(n == 1) or (n >= 3) :
    print(n,"is not a Prime Number")
else:
    print(n,"is a Prime Number")
