
def main():
    print("Amount Due: 50")
    total_amount = 50
    
   

    while total_amount > 0:
        # Takes user input
        user_input = int(input("Insert Coin: "))

        # checks if input is valid
        if user_input in [5, 10, 25]:
            total_amount = total_amount - user_input
            # check if its still sub 50 cents
            if total_amount > 0:
                print("Amount Due: " + str(total_amount))
        else:
            # print("Wrong amount")
            print("Amount Due: " + str(total_amount))


    if total_amount <= 0:
        print("Change Owed: " + str(total_amount * -1))
    else:
        print("Transaction complete")


main()