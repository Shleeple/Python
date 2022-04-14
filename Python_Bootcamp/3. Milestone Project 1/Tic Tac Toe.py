def display_board():
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')


def player_choice():
    marker = input('Enter a number between 1-9: ')
    if marker in board:
        return marker
    elif marker not in board and counter >= 4:
        print("TIC TAC TOE, a tie")
        exit()
    else:
        print('Marker not available')
        return player_choice()


def turn():
    print('Player 1 Turn (X)')
    board[int(player_choice())] = 'X'
    display_board()
    if check_victory():
        return check_victory()

    print('Player 2 Turn (O)')
    board[int(player_choice())] = 'O'
    display_board()
    if check_victory():
        return check_victory()


def check_victory():

    # Checks Horizontal Lines
    if board[1] == board[2] and board[2] == board[3]:
        return board[1]
    elif board[4] == board[5] and board[5] == board[6]:
        return board[4]
    elif board[7] == board[8] and board[8] == board[9]:
        return board[7]

    # Checks Vertical Lines
    elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] and board[5] == board[8]:
        return board[2]
    elif board[3] == board[6] and board[6] == board[9]:
        return board[3]

    # Checks Diagonals
    elif board[1] == board[5] and board[5] == board[9]:
        return board[1]
    elif board[3] == board[5] and board[5] == board[7]:
        return board[3]

    else:
        return False



board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
counter = 0
while check_victory() == False:
    turn()
    if check_victory():
        print(f'The winner is {check_victory()}')
        if input('Do you want to play again? Y or N: ') == 'Y':
            board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            check_victory()
        else:
            print("Thank you for playing, come again")
    counter += 1
    print(f'Counter is {counter}')
