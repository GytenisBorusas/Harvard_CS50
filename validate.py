
import re
import csv


email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("Invalid")







# -----------------------------------------------------------------