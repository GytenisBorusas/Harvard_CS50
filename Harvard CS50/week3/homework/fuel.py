

def main():
    x = get_fuel_amount("Fraction? ")
    print(f"x is {x}")

def get_fuel_amount(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("This isnt a fraction")
        except ZeroDivisionError:
            print("Cant divide by 0")
        else:
            return x
        

main()