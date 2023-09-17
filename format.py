
# import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ?")
#     name = f"{first} {last}"

# print(f"hello, {name}")

# ------------------------------------

# import re

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")

# ------------------------------------

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.groups(1)
print(f"hello, {name}")
