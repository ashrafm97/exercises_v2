import random

user_guess = input("Guess a number mate... between 1 and 3!")
magic_number = random.randint(1, 3)

if user_guess == magic_number:
    print("Super!")
else:
    print(f"Unlucky, it happened to be {magic_number}... better luck next time!")
print(magic_number)

# not sure why there is an error???

