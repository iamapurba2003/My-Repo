#---------------------!Algorithm!--------------------
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
#----------! Global Variables !------------
player_1 = input("Enter Player 1 Name: ")
choice_player1 = input("Enter Player 1's Choice (X / O): ")
choice_2 = "X"
if choice_player1 == "X":
    choice_2 = "O"
else:
    choice_2 = choice_2
player_2 = input("Enter player 2 Name: ")
pos = ['-', '-', '-', '-', '-', '-', '-', '-','-']






#To display board...
def board():
    
    i = 0
    while i <19:
        if i == 0:
            print('-'*49)
        else:
            print(f"| \t  \t | \t  \t |\t  \t|")
        if i == 3:
            print(f"| \t {pos[0]} \t | \t {pos[1]} \t |\t {pos[2]} \t|")
        if i == 6:
            print('-'*49)
        if i == 9:
            print(f"| \t {pos[3]} \t | \t {pos[4]} \t |\t {pos[5]} \t|")
        if i == 12:
            print('-'*49)
        if i == 15:
            print(f"| \t {pos[6]} \t | \t {pos[7]} \t |\t {pos[8]} \t|")
        if i == 18:
            print('-'*49)
            
        i+=1


#Checking for a winner
def winner():
    #horizontal check for "X"
    if pos[0] == pos[1] == pos[2] == "X":
        return True
    elif pos[3] == pos[4] == pos[5] == "X":
        return True
    elif pos[6] == pos[7] == pos[8] == "X":
        return True
    
    #horizontal check for "O"
    elif pos[0] == pos[1] == pos[2] == "O":
        return True
    elif pos[3] == pos[4] == pos[5] == "O":
        return True
    elif pos[6] == pos[7] == pos[8] == "O":
        return True
    
    #vertical check for "X"
    elif pos[0] == pos[3] == pos[6] == "X":
        return True
    elif pos[1] == pos[4] == pos[7] == "X":
        return True
    elif pos[2] == pos[5] == pos[8] == "X":
        return True
    
    #vertical check for "O"
    elif pos[0] == pos[3] == pos[6] == "O":
        return True
    elif pos[1] == pos[4] == pos[7] == "O":
        return True
    elif pos[2] == pos[5] == pos[8] == "O":
        return True
    
    #Diagonal check for "X"
    elif pos[0] == pos[4] == pos[8] == "X":
        return True
    elif pos[2] == pos[4] == pos[6] == "X":
        return True

    #Diagonal check for "O"
    elif pos[0] == pos[4] == pos[8] == "O":
        return True
    elif pos[2] == pos[4] == pos[6] == "O":
        return True
    else:
        return None


#Checking to avoid overwrite
def overwrite(x: int):
    if (pos[x] == "X" or pos[x] == "O"):
        print("The position is already filled, choose other!")
        return True
    else:
        return False


#Swapping the players after taking input from one end...
def swap_players():
    i = 1
    overall = winner()
    while i<10:
        if i%2 != 0:
            board()
            print("{}'s turn".format(player_1))
            player1_pos = int(input("Enter position from 1 to 9: ")) - 1
            write = overwrite(player1_pos)
            while write == True:
                if write == True:
                    player1_pos = int(input()) -1
                    write = overwrite(player1_pos)
                else:
                    break
            pos[player1_pos] = choice_player1
            win = winner()
            if win == True:
                board()
                print(f"{player_1} wins the game!")
                break
            
            
        if i%2 == 0:
            board()
            print(f"{player_2}'s turn")
            player2_pos = int(input("Enter position from 1 to 9: ")) - 1 
            write = overwrite(player2_pos)
            while write == True:
                if write == True:
                    player2_pos = int(input()) -1
                    write = overwrite(player2_pos)
                else:
                    break
            pos[player2_pos] = choice_2
            win2 = winner()
            if win2 == True:
                board()
                print(f"{player_2} wins the game!")
                break


        if i == 9 and overall == None:
            board()
            print("It's a TIE!")
            
        i+=1


#main game
def game():
    swap_players()
    



game()























































