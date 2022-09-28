import random

smallCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '[]{}()*;/.,-_'

combine = smallCase + upperCase + numbers + symbols
print("Welcome to the Secure Password Generator")
print("Just simply input how many digits you need, and it will auto generate it for you (Max. 75)")
length = input("Digits you need : ")
password = "".join(random.sample(combine, int(length)))
print(password)