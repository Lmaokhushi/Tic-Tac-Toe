board = ['-','-','-','-','-','-','-','-','-']

def display():
    print( '|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print( '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print( '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def a(board):
    player1 = "x"
    player2 = "o"

    if board[0] == board[1] == board[2] == player1 or board[0] == board[1] == board[2] == player2:
        return True
    elif board[3] == board[4] == board[5] == player1 or board[3] == board[4] == board[5] == player2:
        return True
    elif board[6] == board[7] == board[8] == player1 or board[6] == board[7] == board[8] == player2:
        return True
    elif board[3] == board[0] == board[6] == player1 or board[3] == board[0] == board[6] == player2:
        return True
    elif board[1] == board[4] == board[7] == player1 or board[1] == board[4] == board[7] == player2:
        return True
    elif board[2] == board[5] == board[8] == player1 or board[2] == board[5] == board[8] == player2:
        return True
    elif board[0] == board[4] == board[8] == player1 or board[0] == board[4] == board[8] == player2:
        return True
    elif board[2] == board[4] == board[6] == player1 or board[2] == board[4] == board[6] == player2:
        return True
    else:
        return False
    
def inpu(board):
    x = int(input("Enter the position : "))
    if board[x-1]!='-':
        print("The value already exists please enter new value!!")
        return inpu(board)
    else:
        return x

player1 = input("Enter name of the player 1 : ")
player2 = input("Enter name of the player 2 : ")
display()
for i in range(9):
    if i%2 == 0:
        x = inpu(board)
        board[x-1] = 'x'
        display()  
        if a(board):
            print(f'Player 1 {player1} wins!!')
            break
    else:
        x = inpu(board)
        board[x-1] = 'o' 
        display() 
        if a(board):
            print(f'Player 2 {player2} wins!!')
            break

print('!!GAME OVER!!')
