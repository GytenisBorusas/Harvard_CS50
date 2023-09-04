
def main():
    user_input = input("Expression: ")
    split_inputs = user_input.split()
    
    x = float(split_inputs[0])
    y = split_inputs[1]
    z = float(split_inputs[2])

    if y == "+":
        print("{:.1f}".format(x + z))
    elif y == "-":
        print("{:.1f}".format(x - z))
    elif y == "*":
        print("{:.1f}".format(x * z))
    else:
        print("{:.1f}".format(x / z))
    




main()    
