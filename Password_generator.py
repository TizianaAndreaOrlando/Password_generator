import random 
from lists import *
#********************   **************   **************
#From here we will input our data
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#********************   **************   **************
#Building our password with for loop

password = []
for number in range(nr_letters):
  password.append(random.choice(letters))
for number in range(nr_symbols):
  password.append(random.choice(symbols))
for number in range(nr_numbers):
  password.append(random.choice(symbols))
print(password)

password = ''.join(password)
print(f"\nYour password is: {password}")