import sys
from pyfiglet import Figlet

def main():
    # Only one additional argument, check if it's a font flag or an error
    if len(sys.argv) == 2:
        sys.exit("Error message #1")  # There's no font name provided after the flag
    # Invalid flag
    elif len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Error message #1")
    # Invalid font or more than 2 additional arguments: exit with an error
    elif len(sys.argv) == 3:
        try:
            # Attempt to create a Figlet object to see if the font is valid
            Figlet(font=sys.argv[2])
        except Exception:
            sys.exit("Error message #1")
    elif len(sys.argv) > 3:
        sys.exit("Error message #1")
    
    # At this point, all errors related to command-line arguments have been checked
    user_input = input("Input: ")

    # No extra arguments, use default 'slant' font
    if len(sys.argv) == 1:
        f = Figlet(font='slant')
    # Two additional arguments: use the provided font
    else:
        f = Figlet(font=sys.argv[2])
    print(f.renderText(user_input))

if __name__ == "__main__":
    main()
