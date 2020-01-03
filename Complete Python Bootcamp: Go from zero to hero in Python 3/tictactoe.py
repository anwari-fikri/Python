def display_board(board):
    print(' {} | {} | {} '.format(board[0],board[1],board[2]))
    print('-----------')
    print(' {} | {} | {} '.format(board[3],board[4],board[5]))
    print('-----------')
    print(' {} | {} | {} '.format(board[6],board[7],board[8]))

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    player = 'unassigned'
    while True:
        if player in 'XxOo' and player != '':
            return player
        elif player == '':
            print('Enter something! Try again.')
        elif player != 'unassigned':
            print('Wrong input! Try again.')
        
        player = input('Do you want to be X or O? ')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    # Horizontal win condition
    if board[0] == board[1] == board[2] == marker:
        return True
    elif board[3] == board[4] == board[5] == marker:
        return True
    elif board[6] == board[7] == board[8] == marker:
        return True
    
    # Vertical win condition
    elif board[0] == board[3] == board[6] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    
    # Diagonal win condition
    elif board[0] == board[4] == board[8] == marker:
        return True
    elif board[2] == board[4] == board[6] == marker:
        return True
    
    else:
        return False

import random

def choose_first():
    return random.randint(0,2)%2==0

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for x in board:
        if x == ' ':
            return False
    return True

def player_choice(board, marker):
    position = int(input(f'{marker}, where do you want to place your marker? (0-8) '))
    while True:
        if space_check(board, position):
            return position
        else:
            print('That space is already occupied!')
            position = int(input('Try another number (0-8): '))

def replay():
    play = input('Press y to play again: ')
    if play in 'Yy' and play != '':
        return True
    else:
        print('Goodbye!')
        return False

while True:
    print('Welcome to Tic Tac Toe!\n')
    game_on = True
    board = ['0','1','2','3','4','5','6','7','8']
    display_board(board)
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker = player_input()
    while game_on:
        if marker in 'Oo':
            position = player_choice(board, marker.upper())
            place_marker(board, marker.upper(), position)
        elif marker in 'Xx':
            position = player_choice(board, marker.upper())
            place_marker(board, marker.upper(), position)

        display_board(board)
        if win_check(board, marker):
            print(f'{marker} WINS!')
            game_on = replay()
            break
        elif full_board_check(board):
            print('Board is full')
            game_on = replay()
            break

        if marker in 'Oo':
            marker = 'X'
        else:
            marker = 'O'
    if game_on == False:
        break