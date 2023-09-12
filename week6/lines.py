
import sys


def main():
    if len(sys.argv) < 2:
        print("Too few comman-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many comman-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith('.py'):
        print("Not a Python file")
        sys.exit(1)
    
    try:
        total_lines = imported_file(sys.argv[1])
        print(f"{total_lines}")
    except FileNotFoundError:
        print("file does not exist")
        sys.exit(1)



def imported_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        non_comment_lines  = [line for line in lines if not line.lstrip().startswith("#")]
        num_lines = len(non_comment_lines)
    return num_lines




if __name__ == "__main__":
    main()