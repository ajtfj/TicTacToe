def display_board(board):
    print('\n'*1000)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_mark():
    mark = ' '

    while mark not in ['X', 'O']:
        mark = input("Player 1: Do you want to be X or O? ").upper()

    if mark == 'X':
        return ('X', 'O')
    else:
        return ('O','X')

def mark_board(board, position, mark):
    board[position] = mark

def is_free(board, position):
   return board[position] == " "

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def player_choice(board):
    position = 0

    while position not in range(1,10) or not is_free(board, position):
        position = int(input("Choose your next position (1-9)"))
    
    return position

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark ) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or 
    (board[7] == board[4] == board[1] == mark) or  
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or 
    (board[9] == board[5] == board[1] == mark))

def full_board_check(board):
    for i in range(1,10):
            if is_free(board, i):
                return False
    return True

def game_turn(borad, player, turn):
    display_board(board)
    print(f"{turn}'s turn!")
    position = player_choice(board)
    mark_board(board, position, player)

    if win_check(board, player):
        display_board(board)
        print(f"Congratulations! {turn} has won the game")
        return False
    else:
        if full_board_check(board):
            display_board(board)
            print("Draw!")
            return False
    return True    

def replay():
    answer = ' '

    while answer not in ['yes', 'no']:
        answer = input("Do you want to pay again? Yes or No ").lower()
    if answer == 'yes':
        return True
    else:
        return False

while True:
    board = [' ']*10
    player1, player2 = player_mark()
    turn = choose_first()

    game_on = True
    while game_on:
        if turn == 'Player 1':
            game_on = game_turn(board, player1, turn)
            turn = 'Player 2'
        else:
            game_on = game_turn(board, player2, turn)
            turn = 'Player 1'
    if not replay():
        break