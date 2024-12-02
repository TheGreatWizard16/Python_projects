import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")

# inputs for password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Check for invalid input
if nr_letters > len(letters) or nr_symbols > len(symbols) or nr_numbers > len(numbers):
    print("Error: You requested more characters than available in the pool.")
else:
    # Generate random parts of the password
    alpha = random.sample(letters, nr_letters)
    sym = random.sample(symbols, nr_symbols)
    num = random.sample(numbers, nr_numbers)

    # Combine all parts and shuffle
    password = alpha + sym + num
    random.shuffle(password)

    # Create the final password
    final_password = ''.join(password)
    print(f"Your randomized password is: {final_password}")
