import random
playing = True
number = str(random.randint(10,20))
print("The random number is ", number)
print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess :
        print("You win th game")
        print("Th number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. \n")