

import re
import sys


def main():
    s = input("HTML: ")
    returned_s = parse(s)
    if returned_s:
        print(returned_s)
    else:
        print(f"No valid URL")


def parse(s):
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s, re.IGNORECASE):
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()



    