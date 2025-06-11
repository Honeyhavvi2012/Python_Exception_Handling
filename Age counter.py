print("Welcome! Please enter your age to check if it's odd or even.")
age_input = input("Enter your age: ")

try:
    age = int(age_input)  
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("Value Error: Please enter a valid whole number for age (no letters, decimals, or symbols).")

print("Best of luck!")
