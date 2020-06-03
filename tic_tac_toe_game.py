import random

def display_board(board):
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    
def player_input():
    marker='wrong'
    while marker not in ['X','O']:
        marker = input("Please pick a marker 'X' or 'O' :").upper()
        if marker not in ['X','O']:
            print('Invalid input!')   
    if marker=='X':
        return('X','O')
    else:
        return('O','X')

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position) :
        position = int(input("Please pick a position between 1-9 :"))
        if position not in range(1,10):
            print('Invalid input!')
            continue
        if not space_check(board,position):
            print('Position already occupied')
            continue
    return position

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    if board[7]== mark and board[8]== mark and board[9]== mark:
        return True
    elif board[4]== mark and board[5]== mark and board[6]== mark:
        return True
    elif board[1]== mark and board[2]== mark and board[3]== mark:
        return True
    elif board[7]== mark and board[5]== mark and board[3]== mark:
        return True
    elif board[7]== mark and board[4]== mark and board[1]== mark:
        return True
    elif board[8]== mark and board[5]== mark and board[2]== mark:
        return True
    elif board[9]== mark and board[6]== mark and board[3]== mark:
        return True
    elif board[1]== mark and board[5]== mark and board[9]== mark:
        return True
    else:
        return False

def choose_first():
    play=random.randint(1, 2)
    if play==1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def replay():
    choice = input("Do you want to play again? 'Y' or 'N' ").upper()
    if choice not in ['Y','N']:
            print('Invalid input!')
    return choice=='Y'

print('Welcome to Tic Tac Toe!')
while True:
    board = [' ']*10
    player1_marker,player2_marker=player_input()
    print('Player 1 marker is {}'.format(player1_marker))
    print('Player 2 marker is {}'.format(player2_marker))
    turn=choose_first()
    print('{} will play first'.format(turn))
    play_game=input("Are you ready to play the game? 'Y','N' : ").upper()
    if play_game=='Y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if (turn=='Player 1'):
            positon=player_choice(board)
            place_marker(board, player1_marker, positon)
            display_board(board)
            if win_check(board, player1_marker):
                print('PLAYER 1 WON!!')
                display_board(board)
                game_on=False
            else:
                if full_board_check(board):
                    print("IT'S A DRAW")
                    display_board(board)
                    game_on=False
                else:
                    turn='Player 2'
                
        if (turn=='Player 2'):
            positon=player_choice(board)
            place_marker(board, player2_marker, positon)
            display_board(board)
            if win_check(board, player2_marker):
                display_board(board)
                print('PLAYER 2 WON!!')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("IT'S A DRAW")
                    game_on=False
                else:
                    turn='Player 1'
    if not replay():
        break