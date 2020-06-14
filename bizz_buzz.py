# user_input = int(input('what number would you like to go up to?'))
# still_wanna_play = input('still wanna play?: y/n ')
# if still_wanna_play.lower() == 'y':
#     while still_wanna_play == True:
#         for i in range(1, (user_input + 1)):
#             if i % 15 == 0:
#                 print('bizzbuzz')
#             elif i % 3 == 0:
#                 print('bizz')
#             elif i % 5 == 0:
#                 print('buzz')
#             else:
#                 print(i)
# else:
#     print('thanks for playing')


def bizz_buzz():
    do_you_wanna_play = input('Do you want to play? y/n')
    while do_you_wanna_play.lower() != 'y':
        return
    else:
        user_input = int(input('what number would you like to go up to?'))
        for i in range(1, (user_input + 1)):
            if i % 15 == 0:
                print('bizzbuzz')
            elif i % 3 == 0:
                print('bizz')
            elif i % 5 == 0:
                print('buzz')
            else:
                print(i)

bizz_buzz()
