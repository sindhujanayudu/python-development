import random
numbers="0123456789"
specialcharacters="!@#$%^&*()"
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#input password length based on the user choice
n=int(input("enter number of numbers"))
s=int(input("enter number of special charaters"))
c=int(input("enter number of characters"))

password=" "
for i in range(n):
    password +=random.choice(numbers)

for j in range(s):
    password +=random.choice(specialcharacters)

for k in range(c):
    password +=random.choice(characters)

print(password)
