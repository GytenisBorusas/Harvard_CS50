# import string

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     forbidden_characters = string.punctuation + " "  # This includes all punctuation marks and space

#     # Check length
#     if not 2 <= len(s) <= 6:
#         return False

#     # Check the first two characters
#     if not (s[0].isalpha() and s[1].isalpha()):
#         return False

#     # Check for forbidden characters
#     for char in s:
#         if char in forbidden_characters:
#             return False

#     # Separate into alphabetic and numeric parts
#     alphabets = ''.join([char for char in s if char.isalpha()])
#     numbers = ''.join([char for char in s if char.isdigit()])
    
#     # Check if the original string is a combination of alphabets followed by numbers
#     if s != alphabets + numbers:
#         return False

#     # Check if the first number is 0
#     if len(numbers) > 0 and numbers[0] == '0':
#         return False

#     return True

# main()




#---------------------------------------------------------------------------------

import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    forbidden_characters = string.punctuation + " "  # This includes all punctuation marks and space

    # Check length
    if not 2 <= len(s) <= 6:
        return False

    # Check the first two characters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for forbidden characters
    for char in s:
        if char in forbidden_characters:
            return False

    # Separate into alphabetic and numeric parts
    alphabets = ''.join([char for char in s if char.isalpha()])
    numbers = ''.join([char for char in s if char.isdigit()])
    
    # Check if the original string is a combination of alphabets followed by numbers
    if s != alphabets + numbers:
        return False

    # Check if the first number is 0
    if len(numbers) > 0 and numbers[0] == '0':
        return False

    return True


if __name__ == "__main__":
    main()