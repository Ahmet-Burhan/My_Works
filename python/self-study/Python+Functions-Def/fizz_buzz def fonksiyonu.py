#Solution 1
def fizz_buzz(num):
    a=[]
    for i in range(1,num+1):
        if not i%15 :
            a.append("FizzBuzz")
        else:
            if not i%5:
                a.append("Buzz")
            else:
                if not i%3:
                    a.append("Fizz")
                else:
                    a.append(i)
    return a
print(fizz_buzz(15))

#Solution 2
def fizzbuzz(num):
    return["FizzBuzz" if not n%15 else "Buzz" if not n%5 else "Fizz" if not n%3 else n for n in range(1,num+1)]
print(fizzbuzz(15))
