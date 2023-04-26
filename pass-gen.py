import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{};:<,.">/?`~'

length = input("Enter the length of the password you need (Max. 75): ")
length = min(int(length), 75) if length.isdigit() else 10

password = ''.join(random.choice(chars) for _ in range(length))
print("Your new password is:", password)