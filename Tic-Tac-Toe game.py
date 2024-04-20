def display_board(board):
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
test_board=['#','X','O','X','O','X','O','X','O','X']

def player_input():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker = input('Player1, choose X or O : ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')    

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    return board[position]==' '

def player_choice(board):
    while True:
        position=input('Choose your option (1-9): ')
        if position.isdigit() and int(position) in range(1,10) and space_check(board,int(position)):
            return int(position)
        else:
            print('Invalid input. please enter a number between 1 and 9')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or 
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or 
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

def full_board_check(board):
    return ' ' not in board[1:]

def game_over(board,mark):
    if win_check(board,mark):
        display_board(board)
        print(f'Player {mark} has won the game!')
        return True
    elif full_board_check(board):
        display_board(board)
        print("It's a Draw!")
        return True
    return False

def replay():
    return input('Do you want to play again? Enter Y or N').lower().startswith('y')

print('Welcome to Tic Tac Toe!')
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first.')
    game_on=False
    while True:
        play_game=input('Are you ready to play? Enter Y or N.').upper()
        if play_game=='Y':
            game_on=True
            break
        elif play_game=='Y':
            game_on=False
            break
        else:
            print('Invalid input. Please enter Y or N.')
    if not game_on:
        break           
    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if game_over(the_board,player1_marker):
                break
            else:
                turn='Player2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if game_over(the_board,player2_marker):
                break
            else:
                turn='Player1'
    if not replay():
        break
