

import re
import sys


def main():
    s = input("Input: ").strip()
    returned_um_count = count(s)
    print(f"{returned_um_count}")
    
def count(s):
    um_count = len(re.findall(r'\bum\b', s, re.IGNORECASE))
    return um_count



if __name__ == "__main__":
    main()


