name = input("what is your name? ")
# print(f"Welcome {name.title()}, I hope you enjoy your time here. :)")

age = int(input("How old are you? "))
def birthday_check():
    birthday_gone = input("Has your birthday gone this year? Yes or no? ")
    if birthday_gone.lower() == "yes":
        return 2020 - age
    else:
        return (2020 - age) - 1
# def date_of_birth:
#     if birthday_gone:
#         return age + 1
#     else:
#         return age

print(f'Wow, {name.title()}, you are {age} and were born in {birthday_check()} right?')
