

url = input("URL: ").strip()

username = url.replace("http://twitter.com/", "")
print(f"Username: {username}")