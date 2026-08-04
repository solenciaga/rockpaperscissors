import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Make your move! - Rock, Paper, Scissors, or Quit')
        player_input = input('>')
        if player_input == 'q':
            sys.exit()
        if player_input == 'r' or player_input == 'p' or player_input == 's':
            break
        print('Type one of r, p, s, or q.')

    if player_input == 'r':
        print('Rock vs..')
    elif player_input == 's':
        print('Scissors vs..')
    elif player_input == 'p':
        print('Paper vs..')

    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 's'
        print('SCISSORS')
    elif move_number == 3:
        print('PAPER')
        computer_move = 'p'

    if player_input == computer_move:
        print('Tie!')
        ties = ties + 1
    elif player_input == 'r' and computer_move == 's':
        print('You won!')
        wins = wins + 1
    elif player_input == 'p' and computer_move == 'r':
        print('You won!')
        wins  = wins + 1
    elif player_input == 's' and computer_move == 'p':
        print('You won!')
        wins = wins + 1
    elif player_input == 'r' and computer_move == 'p':
        print('You Lost!')
        losses = losses + 1
    elif player_input == 'p' and computer_move == 's':
        print('You Lost!')
        losses = losses + 1
    elif player_input == 's' and computer_move == 'r':
        print('You Lost!')
        losses = losses + 1

