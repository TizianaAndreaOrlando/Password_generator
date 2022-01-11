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
for number in range(1,nr_letters + 1):
  password.append(random.choice(letters))
for number in range(1,nr_symbols + 1):
  password.append(random.choice(symbols))
for number in range(1,nr_numbers + 1):
  password.append(random.choice(symbols))

#********************   **************   **************
# We will change the password order to make it safer.

password = random.sample(password,len(password))
password = ''.join(password) 
print(f"\nYour password is: {password}")
