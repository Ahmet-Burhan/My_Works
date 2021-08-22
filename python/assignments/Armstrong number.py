while True :
    number = input("enter a positive integer number : ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, " is invalid entry. Enter valid input.!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number. Sorry.")
            break
