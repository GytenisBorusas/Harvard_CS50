

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    if matches := re.search(r"^https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)$", url, re.IGNORECASE):
        print(f"Match URL:", matches.group(1))

    return 


if __name__ == "__main__":
    main()



    