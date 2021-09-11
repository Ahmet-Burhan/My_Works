while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two  # normal part of the program
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")  # executes when division by zero
    else:
        print("The result of the division is : ", division)  # executes if there is no exception
    finally:
        print("Thanks for using our mini divison calculator! Come again!")
        break  # exits the while loop         


try:
    x = 4/1
except:
    print("error")
else:
    print("fine") 
finally:
    f.close()

try:
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')




########################################################
fruits = ["banana","mango","pear","apple","kiwi","grape"]
count=3
while count > 0:
    try:
        index = int(input("Pick an index number to choose your favorite fruit :"))
        print("Your favorite fruit is",fruits[index] )
    except IndexError:
        count -= 1
        print(f"There is no such an Index. You have {count} tries remaining. Try again!")
    except ValueError:
        count -= 1
        print(f"You should enter integer. You have {count} tries remaining. Try again!")
    else:
        print("Congrats! You have entered a valid input.")
        break
    finally:
        print("Out fruits are always fresh!")


#########son