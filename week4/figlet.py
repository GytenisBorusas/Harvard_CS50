import sys
from pyfiglet import Figlet

def main():
    user_input = input("Input: ")

    # No extra arguments, use default 'slant' font
    if len(sys.argv) == 1:
        f = Figlet(font='slant')
        print(f.renderText(user_input))
    # Only one additional argument, check if it's a font flag or an error
    elif len(sys.argv) == 2:
        sys.exit("Error message #1")  # There's no font name provided after the flag
    # Two additional arguments: should be font flag + font name
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            # Use the provided font
            f = Figlet(font=sys.argv[2])
            print(f.renderText(user_input))
        else:
            sys.exit("Error message #1")  # Invalid flag
    # More than 2 additional arguments is an error
    else:
        sys.exit("Error message #2")

if __name__ == "__main__":
    main()
