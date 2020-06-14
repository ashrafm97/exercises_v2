my_response = ''
def mr_miyagi():
    if my_response.endswith("?"):
        print('Questions are not for you! Wax on wax off.')
    elif not my_response.capitalize().startswith('Sensei'):
        print('Address me with respect, Mike Shounen!')
    elif my_response.count('block') or my_response.count('blocking') >=1:
        print('Best block is not be there! Move!')
    else:
        print('Do NOT lose focus... wax on, wax off!')

while my_response != 'Sensei, I am at peace':
    my_response = input('I am listening, Mike-san...')
    if(my_response == 'Sensei, I am at peace'):
        break
    mr_miyagi()

print('Sometimes what heart know, head forget! Goodbye, Mike-san...')
