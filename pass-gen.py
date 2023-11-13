import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    length = input("Enter the length of the password you need (between 8 and 75): ")
    if length.isdigit():
        length = int(length)
        if 8 <= length <= 75:
            break
    print("Invalid input. Please enter a valid positive integer between 8 and 75.")

password = ''.join(random.choice(chars) for _ in range(length))
print("Your new password is:", password)
