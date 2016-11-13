print 'Welcome to Tic Tac Toe!'

board = [['','',''],['','',''],['','','']]

###Print Board function###
def print_board(board):
    for sublist in board:
        print sublist
        
###Raw input only allowable###
def player_input():
    x = raw_input()
    while x != '0' and x != '1' and x != '2':
        print 'Input not allowed %s, select 0, 1 or 2!'%x
        x = raw_input()
    return x

###Move for Player 1 -- 'X'###
def player_1(x,y):
    global board
    if board[x][y] == '':
        board[x][y] = 'X'
        return print_board(board)
    else:
        print 'Already taken, please select again!'
        print '%s, what is your move? (Row)' %Player_1
        row = player_input()
        print '%s, what is your move? (Column)' %Player_1
        column = player_input()
        
        player_1(int(row),int(column))
        return print_board(board)

###Move for Player 2 -- 'O'###
def player_2(x,y):
    global board
    if board[x][y] == '':
        board[x][y] = 'O'
    else:
        print 'Already taken, please select again!'
        print '%s, what is your move? (Row)' %Player_2
        row = player_input()
        print '%s, what is your move? (Column)' %Player_2
        column = player_input()
        player_2(int(row),int(column))
    return print_board(board)

###Checks if board is full###
def board_full(board):
    for sublist_rows in board:
        for place in sublist_rows:
            if place == '':
                return False
    return True


###Checks if Tic Tac Toe is reached###
def tic_tac_toe(board):
    
    for sublist_rows in board:
        if len(set(sublist_rows)) == 1:
            for place in sublist_rows:
                if place != '':
                    return True
    
    col_0 = [col[0] for col in board]
    col_1 = [col[1] for col in board]
    col_2 = [col[2] for col in board]

    flipped_board = []

    flipped_board.append(col_0)
    flipped_board.append(col_1)
    flipped_board.append(col_2)
        
    for sublist_rows in flipped_board:
        if len(set(sublist_rows)) == 1:
            for place in sublist_rows:
                if place != '':
                    return True
                
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '':
            return True
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '':
        return True
    
    return False
                
#while


###Actual game play back in forth. Need to add 'While' loop to end game when Tic Tac Toe is reached or board is full###
print 'Player 1 - What is your name?'
Player_1 = raw_input()

print 'Player 2 - What is your name?'
Player_2 = raw_input()

while tic_tac_toe(board) == False and board_full(board) == False:
    print '%s, what is your move? (Row)' %Player_1
    row = player_input()
    print '%s, what is your move? (Column)' %Player_1
    column = player_input()
    player_1(int(row),int(column))
    if tic_tac_toe(board) == True:
        print '%s wins!' %Player_1
        break
    elif board_full(board) == True:
        print 'Game over! Tie game.'
        break
    print '%s, what is your move? (Row)' %Player_2
    row = player_input()
    print '%s, what is your move? (Column)' %Player_2
    column = player_input()
    player_2(int(row),int(column))
    if tic_tac_toe(board) == True:
        print '%s wins!' %Player_2
        break
    elif board_full(board) == True:
        print 'Game over! Tie game.'
        break
