#Write a program that takes a number from the user, assigns it to the variable (number), and prints the squares of all numbers between 0 and the number (not included) entered by the user.

#Note: Write the program with while statement.

number = int(input('Please enter a number: '))
i= 0
while i < number:
    print(i ** 2)
    i += 1
