letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
t=nr_symbols+nr_numbers+nr_letters
a=[]
for i in range(0,nr_letters):
    d=random.randint(0,51)
    f=letters[d]
    a.append(f)
for j in range(0,nr_numbers):
    c=random.randint(0,9)
    f=numbers[c]
    a.append(f)
for k in range(0,nr_symbols):
    b=random.randint(0,8)
    f=symbols[b]
    a.append(f)

ch=""
for i in range(0,t):
    d=random.choice(a)
    ch+=d
    a.remove(d)
print(ch)