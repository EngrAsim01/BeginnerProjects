import random

print(f'                              --------------------------------\n'
      f'                             |                                |\n'
      f'                             |      Double six Dice Game      |\n'
      f'                             |                                |\n'
      f'                              -------------------------------- \n'
      f'\n')
while True:
    player1 = input('Player1: Enter your name: ')

    counter1 = 1

    while True:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == 6 and dice2 == 6:
            print(f'Dice1: {dice1} Dice2: {dice2}  No of counts: {counter1}')
            break
        else:
            print(f'Dice1: {dice1} Dice2: {dice2}')
            counter1 +=1
            continue

    player2 = input('Player2: Enter your name: ')

    counter2 = 1

    while True:

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 6 and dice2 == 6:
            print(f'Dice1: {dice1} Dice2: {dice2}  No of counts: {counter2}')
            break
        else:
            print(f'Dice1: {dice1} Dice2: {dice2}')
            counter2 +=1
            continue

    if counter1 < counter2:
        print(f'{player1} wins..')
    elif counter1 == counter2:
        print('Draw')
        break
    else:
        print(f'{player2} wins..')

