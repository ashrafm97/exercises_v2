restaurant_menu = ['falafel', 'hummus', 'couscous', 'beans on toast']
# this is the menu
food_order = []
# empty list we wanna append to
no_of_orderers = int(input('Table for how many?'))
print(f"Table for {no_of_orderers} right over here guys!")
print("Items on today's menu include: ")
for food in restaurant_menu:
    print(food.title())

# no of ppl ordering

order = []
# empty order list for customers
while no_of_orderers != 0:
    user_order = input("what do you wanna eat? ")
    user_order = user_order.lower()
    while(restaurant_menu.count(user_order)<1):
        print("Not on the menu, sorry!")
        user_order = input("what do you wanna eat? ")
    order.append(user_order)
    print("Your order so far:  ")
    for food in order:
        print(food)
    no_of_orderers -= 1
    print(f"You may order {no_of_orderers} more times. :) ")
    print()
    if no_of_orderers == 0:
        print("Gonna make that now! One minute!")
        break
