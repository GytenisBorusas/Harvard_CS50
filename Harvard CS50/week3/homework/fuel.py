

def main():
    fuel_fraction = get_fuel_amount("Fraction? ")

    # divides input 'fuel_fraction' into 2 different variables - 'x' and 'y'
    x, y = fraction_input.split('/')

    # Converts 'x' and 'y' to integers
    x = int(x)
    y = int(y)

    fuel_amount = x / y * 100
    print(f"{fuel_amount}")





# def get_fuel_amount(prompt):
#     while True:
#         try:
#             x = int(input(prompt))
#         except ValueError:
#             print("This isnt a fraction")
#         except ZeroDivisionError:
#             print("Cant divide by 0")
#         else:
#             return x
        

main()