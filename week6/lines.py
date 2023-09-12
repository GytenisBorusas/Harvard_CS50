
import sys


def main():
    total_lines = imported_file()
    print(f"{total_lines}")




def imported_file():
    with open("hello.py", "r") as file:
        lines = file.readlines()
        non_comment_lines  = [line for line in lines if not line.lstrip().startswith("#")]
        num_lines = len(non_comment_lines)
    return num_lines




if __name__ == "__main__":
    main()