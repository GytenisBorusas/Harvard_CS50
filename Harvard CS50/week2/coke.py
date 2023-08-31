
def main():
    print("Amount Due: 50")
    total_amount = 50 - 0
    
   

    while total_amount > 0:
        user_input = input("Insert Coin: ")
        if total_amount > 0:
            if user_input == 5 or user_input == 10 or user_input == 25:
                total_amount = total_amount - int(user_input)
                print("Amount Due: " + str(total_amount))
        else:
            if total_amount < 0:
                print("Amount Owed: " + str(total_amount))
  






    # amount_owed = total_amount(user_input)




main()
