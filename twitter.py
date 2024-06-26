
import re

url = input("URL: ").strip()


# username = re.sub(r"^(https?//)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")


# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

#same as above
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

