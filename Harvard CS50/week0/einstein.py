
def main():
    user_input = input("m: ")  # m = mass
    mass = int(user_input)
    joules = mass * 300000000 * 300000000 # E=mc^2
    print("E = " + str(joules))

main()
    