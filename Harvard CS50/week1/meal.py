
def main():
    time = input("What time it is? ")   # Asks user to define time and takes it as an input

    decimal_time = convert(time)

    if  7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(':')
    
    hours = int(hours)
    minutes = int(minutes)

    decimal_time = hours + (minutes / 60)

    return decimal_time


if __name__ == "__main__":
    main()
