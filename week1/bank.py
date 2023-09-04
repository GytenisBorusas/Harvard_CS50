
# def main():
#     user_input = input("Greeting: ")
#     user_input = user_input.lower()
#     user_input = user_input.replace(" ", "")
#     symbols = list(user_input)
# 
#    hello_list = ['h', 'e', 'l', 'l', 'o']
    # h_list = ['h']

    # if symbols[0:5] == hello_list:
    #     print("$0")
    # elif symbols[0] == ['h]']:
    #     print("$20")
    # else:
    #     print("$100")
    #     
    #     # test variables
    #     print(symbols[0:5])

def main():
    user_input = input("Greeting: ")   
    user_input = user_input.lower()
    user_input = user_input.replace(" ", "")

    
    if user_input.startswith("hello"):
        print("$0")
    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")








main()