# We will prepare board for the chess game
# Asking user for color choice
#Swap players
#Cutting or eleminating the opponent's card

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

chess_pos = ['Bishop', 'Knight', 'Rook', 'King', 'Queen', 'Pawns', '     ']

def chessboard():
    i = 0
    while i<33:
        if i == 0:
            print('-'*66, i)
        
        elif i == 2:
            print(f"|  {chess_pos[2]}  | {chess_pos[1]}| {chess_pos[0]}| {chess_pos[4]} | {chess_pos[3]}  | {chess_pos[0]}| {chess_pos[1]}| {chess_pos[2]}  |", i)
        
        elif i == 4:
            print('-'*66,i)

        elif i == 6:
            print(f"| {chess_pos[5]}  | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} |", i)
        
        elif i == 8:
            print('-'*66,i)
        
        elif i == 10:
            print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

        elif i == 12:
            print('-'*66,i)
        
        elif i == 14:
            print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

        elif i == 16:
            print('-'*66,i)
        
        elif i == 18:
            print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

        elif i == 20:
            print('-'*66,i)
        
        elif i == 22:
            print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

        elif i == 24:
            print('-'*66,i)
        
        elif i == 26:
            print(f"| {chess_pos[5]}  | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} |", i)
                
        elif i == 28:
            print('-'*66,i)
        
        elif i == 30:
            print(f"|  {chess_pos[2]}  | {chess_pos[1]}| {chess_pos[0]}| {chess_pos[4]} | {chess_pos[3]}  | {chess_pos[0]}| {chess_pos[1]}| {chess_pos[2]}  |", i)
        
        elif i == 32:
            print('-'*66,i)

        else:
            print("| \t | \t | \t | \t | \t | \t | \t | \t |", i)
        
        i+=1


chessboard()























