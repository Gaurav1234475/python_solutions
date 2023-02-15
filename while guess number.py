run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input == 7:
        print('You won!')
        run = False
    else:
        print('try again!')
        continue