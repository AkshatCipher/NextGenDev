import numpy
import string
import random

l=int(input("Enter length of password:"))

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Your Random password is:", password)

no=1
while no==1:
    password(l)
    print("Do you want a different password?")
    print("1. Yes")
    print("2. No")
    ch=int(input("Enter your choice (1/2): "))
    no=ch