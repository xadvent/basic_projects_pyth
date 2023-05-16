import secrets
import string
import os

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation
all_char = letters + numbers + special

os.system('cls' if os.name == 'nt' else 'clear')

length = 8
pwd = ''
for i in range(length):
    pwd += ''.join(secrets.choice(all_char))

print(pwd)

