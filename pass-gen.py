import random

smallCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '[]{}()*;/.,-_'

combine = smallCase + upperCase + numbers + symbols
length = input("Digits you need (in numbers) : ")
password = "".join(random.sample(combine, int(length)))
print(password)