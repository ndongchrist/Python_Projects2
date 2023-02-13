from random import randrange
play = True

board = ['1','2','3','4','5','6','7','8','9'] #defining a board 

#Display the board
def display():
    print("- - - - - - -")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("- - + - + - -")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("- - + - + - -")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("- - - - - - -")

def fillBox(player):
    box = input(f"{player} choose your box >")
    
    if box == '1':
        if board[0] != "O" or "X":
            board[0] = player
        else:
            print("already taken")
            
            
    if board[0] != player:
        if box == '2':
            board[1] = player
            
    if board[2] != player:
        if box == '3':
            board[2] = player
            
    if board[3] != player:
        if box == '4':
            board[3] = player
            
    if board[4] != player:
        if box == '5':
            board[4] = player
            
    if board[5] != player:
        if box == '6':
            board[5] = player
            
    if board[6] != player:
        if box == '7':
            board[6] = player
            
    if board[7] != player:
        if box == '8':
            board[7] = player
            
    if board[8] != player:
        if box == '9':
            board[8] = player


#taking user input
    

    
def winner(player):  
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[4] == board[8] or
        board[4] == board[6] == board[2] or
        board[3] == board[0] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8]):
        print(f"{player} wins")
        play=False
        
    else:
        pass
    
print("Welcome to my tictactoe")
computer = ""
player = input("Choose bwtween `O` and `X`")
if player == "O":
    computer = 'X'
    
else:
    computer = "O"
      
while play != False:
    display()
    fillBox(player)
    fillBox(computer)
    winner(player)
    winner(computer)

    
        

