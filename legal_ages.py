age = 19
drivers_license = True

user_input = ''
print('Type exit to exit the loop!')
while user_input != 'exit':
    user_input = input('exit?')
    if user_input.lower() == exit:
        break
    age = int(input('how old are you?'))
    drivers_license_input = input("do you have a license? y/n ")

    if(drivers_license_input.lower() == 'y'):
        drivers_license = True
    else:
        drivers_license = False

    if(age > 19 and drivers_license == False):
        print('freeedom')
    elif age > 19:
        print('go vote g >:)')
    elif 17<age<18:
        print('enjoy ur youth')
    else:
        print('go to skl')




# if age == 19 and drivers_license == True:
#     print('Enjoy your freedom')
