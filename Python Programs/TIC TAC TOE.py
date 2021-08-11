#---------------------!Algorithm!--------------------
#Ask for player choice {Player v Player} or {Player v System[Beta]}
#Input player names
#Ask for 'X' or 'O'
#position 
#Display the board 
#Ask user for input 
#swap players
#prohibit overwrite
#continuous check for winner
    #Display Winner with name...

#------------------! Main Code !----------------------
#-------! Modules !---------
import random

#----------! Global Variables !------------
pos = ['', ' ', '', ' ', ' ', '', '', ' ',' ']
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

try:
    play_choice = int(input("1.PvP\n2.PvSys\nEnter num choice: "))



    if play_choice == 1:
        player_1 = input("Enter Player 1 Name: ")
        if player_1 == "":
            player_1 = "Player 1"
        choice_player1 = input("Enter Player 1's Choice (X / O): ")
        choice_2 = "X"
        if choice_player1 == "X":
            choice_2 = "O"
        else:
            choice_2 = choice_2
        player_2 = input("Enter player 2 Name: ")
        if player_2 == "":
            player_2 = "Player 2"

    if play_choice == 2:
        player = input("Enter player's name: ")
        if player == "":
            player = "Player"
        sys_choice = "X"
        choice_player = input("Enter choice (X / O): ")
        if choice_player == 'X':
            sys_choice = "O"
        else:
            sys_choice = sys_choice
except Exception:
    print("Enter a valid input!")
    try:
        play_choice = int(input())
        player = input("Enter player's name: ")
        sys_choice = "X"
        choice_player = input("Enter choice (X / O): ")
        if choice_player == 'X':
            sys_choice = "O"
    except Exception:
        print("Thanks for playing!")
        exit()
    

#To display board...
def board():
    
    i = 0
    while i <19:
        if i == 0:
            print(f'{BLUE}-{RESET}'*49)
        else:
            print(f"{BLUE}| \t  \t | \t  \t |\t  \t|{RESET}")
        if i == 3:
            print(f"{BLUE}| \t {GREEN}{pos[0]}{RESET}{BLUE} \t | \t {GREEN}{pos[1]}{RESET}{BLUE} \t |\t {GREEN}{pos[2]}{RESET}{BLUE} \t|{RESET}")
        if i == 6:
            print(f'{BLUE}-{RESET}'*49)
        if i == 9:
            print(f"{BLUE}| \t {GREEN}{pos[3]}{RESET}{BLUE} \t | \t {GREEN}{pos[4]}{RESET}{BLUE} \t |\t {GREEN}{pos[5]}{RESET}{BLUE} \t|{RESET}")
        if i == 12:
            print(f'{BLUE}-{RESET}'*49)
        if i == 15:
            print(f"{BLUE}| \t {GREEN}{pos[6]}{RESET}{BLUE} \t | \t {GREEN}{pos[7]}{RESET}{BLUE} \t |\t {GREEN}{pos[8]}{RESET}{BLUE} \t|{RESET}")
        if i == 18:
            print(f'{BLUE}-{RESET}'*49)

        


        i+=1


#Checking for a winner
def winner():
    #horizontal check for "X"
    if pos[0] == pos[1] == pos[2] == "X" or pos[0] == pos[1] == pos[2] == "O":
        return True
    elif pos[3] == pos[4] == pos[5] == "X" or pos[3] == pos[4] == pos[5] == "O":
        return True
    elif pos[6] == pos[7] == pos[8] == "X" or pos[6] == pos[7] == pos[8] == "O":
        return True
    
    # #horizontal check for "O"
    # elif pos[0] == pos[1] == pos[2] == "O":
    #     return True
    # elif pos[3] == pos[4] == pos[5] == "O":
    #     return True
    # elif pos[6] == pos[7] == pos[8] == "O":
    #     return True
    
    #vertical check for "X"
    elif pos[0] == pos[3] == pos[6] == "X" or pos[0] == pos[3] == pos[6] == "X":
        return True
    elif pos[1] == pos[4] == pos[7] == "X" or pos[1] == pos[4] == pos[7] == "O":
        return True
    elif pos[2] == pos[5] == pos[8] == "X" or pos[2] == pos[5] == pos[8] == "O":
        return True
    
    #vertical check for "O"
    elif pos[0] == pos[3] == pos[6] == "O":
        return True
    # elif :
    #     return True
    # elif :
    #     return True
    
    # #Diagonal check for "X"
    elif pos[0] == pos[4] == pos[8] == "X" or pos[0] == pos[4] == pos[8] == "O":
        return True
    elif pos[2] == pos[4] == pos[6] == "X" or pos[2] == pos[4] == pos[6] == "O":
        return True

    else:
        return None


#Checking to avoid overwrite
def overwrite(x: int):
    if (pos[x] == "X" or pos[x] == "O"):
        return True
    else:
        return False


#Swapping the players after taking input from one end...
def swap_players():
    i = 1
    overall = winner()
    while i<10:
        if play_choice == 1:
            if i%2 != 0:
                if i == 1:
                    board()
                    print("{}'s turn".format(player_1))
                    print("Your choice is {}".format(choice_player1))
                    player1_pos = int(input("Enter position from 1 to 9: ")) - 1
                    write = overwrite(player1_pos)
                    while write == True:
                        if write == True:
                            print("The position is already filled, choose other!")
                            player1_pos = int(input()) -1
                            write = overwrite(player1_pos)
                        else:
                            break
                    pos[player1_pos] = choice_player1
                    win = winner()
                    if win == True:
                        board()
                        print(f"{RED}{BOLD}{player_1}{RESET} wins the game!")
                        break
                
                if i!= 1:
                    board()
                    print("{}'s turn".format(player_1))
                    print("Your choice is {}".format(choice_player1))
                    player1_pos = int(input("Enter position from leftover places: ")) - 1
                    write = overwrite(player1_pos)
                    while write == True:
                        if write == True:
                            print("The position is already filled, choose other!")
                            player1_pos = int(input()) -1
                            write = overwrite(player1_pos)
                        else:
                            break
                    pos[player1_pos] = choice_player1
                    win = winner()
                    if win == True:
                        board()
                        print(f"{RED}{BOLD}{player_1}{RESET} wins the game!")
                        break
                
            if i%2 == 0:
                if i == 2:
                    board()
                    print(f"{player_2}'s turn")
                    print("Your choice is {}".format(choice_2))
                    player2_pos = int(input("Enter position from 1 to 9: ")) - 1 
                    write = overwrite(player2_pos)
                    while write == True:
                        if write == True:
                            print("The position is already filled, choose other!")
                            player2_pos = int(input()) -1
                            write = overwrite(player2_pos)
                        else:
                            break
                    pos[player2_pos] = choice_2
                    win2 = winner()
                    if win2 == True:
                        board()
                        print(f"{YELLOW}{BOLD}{player_2}{RESET} wins the game!")
                        break
                if i != 2:
                    board()
                    print(f"{player_2}'s turn")
                    print("Your choice is {}".format(choice_2))
                    player2_pos = int(input("Enter position from leftover places: ")) - 1 
                    write = overwrite(player2_pos)
                    while write == True:
                        if write == True:
                            print("The position is already filled, choose other!")
                            player2_pos = int(input()) -1
                            write = overwrite(player2_pos)
                        else:
                            break
                    pos[player2_pos] = choice_2
                    win2 = winner()
                    if win2 == True:
                        board()
                        print(f"{YELLOW}{BOLD}{player_2}{RESET} wins the game!")
                        break
        if play_choice == 2:
            if choice_player == "X":
                if i%2 != 0:
                    if i == 1:
                        board()
                        print("{}'s turn".format(player))
                        print("Your choice is {}".format(choice_player))
                        player_pos = int(input("Enter position from 1 to 9: ")) - 1
                        write = overwrite(player_pos)
                        while write == True:
                            if write == True:
                                print("The position is already filled, choose other!")
                                player_pos = int(input()) -1
                                write = overwrite(player_pos)
                            else:
                                break
                        pos[player_pos] = choice_player
                        win = winner()
                        if win == True:
                            board()
                            print(f"{BOLD}{GREEN}{player}{RESET} wins the game!")
                            break
            
                    if i != 1:
                        board()
                        print("{}'s turn".format(player))
                        print("Your choice is {}".format(choice_player))
                        player_pos = int(input("Enter position from leftover places: ")) - 1
                        write = overwrite(player_pos)
                        while write == True:
                            if write == True:
                                print("The position is already filled, choose other!")
                                player_pos = int(input()) -1
                                write = overwrite(player_pos)
                            else:
                                break
                        pos[player_pos] = choice_player
                        win = winner()
                        if win == True:
                            board()
                            print(f"{BOLD}{GREEN}{player}{RESET} wins the game!")
                            break
            
                if i%2 == 0:
                    board()
                    print("System's turn")
                    sys_turn = random.randint(0, 8)
                    write = overwrite(sys_turn)
                    while write == True:
                        if write == True:
                            print("Re-choosing the position...")
                            sys_turn = random.randint(0,8)
                            write = overwrite(sys_turn)
                        else:
                            break
                    print("System's turn complete...")
                    pos[sys_turn] = sys_choice
                    win = winner()
                    if win == True:
                        board()
                        print(f"{BOLD}{RED}Computer{RESET} wins the game!")
                        break

                
            if choice_player == "O":
                if i%2 == 0:
                    board()
                    print("{}'s turn".format(player))
                    print("Your choice is {}".format(choice_player))
                    player_pos = int(input("Enter position from 1 to 9: ")) - 1
                    write = overwrite(player_pos)
                    while write == True:
                        if write == True:
                            print("The position is already filled, choose other!")
                            player_pos = int(input()) -1
                            write = overwrite(player_pos)
                        else:
                            break
                    pos[player_pos] = choice_player
                    win = winner()
                    if win == True:
                        board()
                        print(f"{BOLD}{YELLOW}{player}{RESET} wins the game!")
                        break
            
                if i%2 != 0:
                    board()
                    print("System's turn")
                    sys_turn = random.randint(1, 10)
                    write = overwrite(sys_turn)
                    while write == True:
                        if write == True:
                            print("Re-choosing the position...")
                            sys_turn = random.randint(1,10)
                            write = overwrite(sys_turn)
                        else:
                            break
                    print("System's turn complete...")
                    pos[sys_turn] = sys_choice
                    win = winner()
                    if win == True:
                        board()
                        print(f"{BOLD}{RED}Computer{RESET} wins the game!")
                        break
        if i == 9 and overall == None:
            board()
            print("No one wins :( !")
            
        i+=1


#main game
def game():
    
    swap_players()
    
game()























































