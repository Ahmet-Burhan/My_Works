saved_amount = int(input('Please enter your saved amount: '))
ps4_price = 400
if saved_amount < ps4_price/2:
    print("You must save more, keep saving!")
elif saved_amount < ps4_price:
    print("You saved more than half, keep saving!")
else :
    print("Yippee! You can buy your PS4")
