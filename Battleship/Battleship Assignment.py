import random

 # an array of emptyness that has a defult value of false, to show its not hit or filled by a ship yet
 #this sets up the shape and size of the bord by making the arrary
gameboard = [[False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False]]

# setting up the layout of the board

def printGame(gameboard): #pass in the board to minipulate it and create the columns and rows
    print("  1 2 3 4 5 6 7 8")
    counter = 1
    for i in gameboard:
        print(str(counter)+"",end=" ")
        for j in i:
            # does the setting up of the gameboard
            if(j==False):
                print("X",end=" ")
            elif(j==True):
                print("H",end=" ")
            elif(j=="E"):
                print("E",end=" ")
            elif(j=="D"):
                print("D",end=" ")
            elif (j == "B"):
                print("B", end=" ")
            elif (j == "A"):
                print("A", end=" ")
            elif (j=="H"):
                print("H", end=" ")
            elif (j=="M"):
                print("M", end=" ")
        counter +=1
        print(" ")

#randomizes the ship placement
def placeShips(gameboard): 
    ships = []
    i = random.randint(1,2)
    if(i==1):
        v = random.randint(0,6) #generates random number
        h = random.randint(0,4)
        gameboard[h][v]="E"
        gameboard[h][v+1]="E"
        l = [i,h,v,0]
        ships.append(l)
    else:
        v = random.randint(0,7) 
        h = random.randint(0,3)
        gameboard[h][v]="E"
        gameboard[h+1][v]="E"
        l = [i, h, v,0]
        ships.append(l) #appends to the list
    i = random.randint(1,2)

    if(i==1):
        while(True): #Destroyer - size 3
            v = random.randint(0, 5)
            h = random.randint(0, 4)
            if (gameboard[h][v] == False):
                if (gameboard[h][v+1] == False):
                    if (gameboard[h][v+2] == False):
                        gameboard[h][v] = "D"
                        gameboard[h][v+1] = "D"
                        gameboard[h][v+2] = "D"
                        l = [i, h, v,0]
                        ships.append(l)
                        break

                # the above is the acutal fucntion for each ship
                # it sets the size of the ship and the letter it needs to
                # represent, from there we use with with the gamebord to make
                # sure that none of the ships overlalp with eachother
    else:
        #Destroyer - size 3
        while(True):
            v = random.randint(0,7)
            h = random.randint(0,2)
            if(gameboard[h][v]==False):
                if(gameboard[h+1][v]==False):
                    if(gameboard[h + 2][v] ==False):
                        gameboard[h][v]="D"
                        gameboard[h+1][v]="D"
                        gameboard[h+2][v]="D"
                        l = [i, h, v,0]
                        ships.append(l)
                        break

    i = random.randint(1, 2)
    if (i == 1):
        while (True):
            v = random.randint(0, 4) #Battleship - size 4
            h = random.randint(0, 4)
            if (gameboard[h][v] == False):
                if (gameboard[h][v + 1] == False):
                    if (gameboard[h][v + 2] == False):
                        if (gameboard[h][v + 3] == False):
                            gameboard[h][v] = "B"
                            gameboard[h][v + 1] = "B"
                            gameboard[h][v + 2] = "B"
                            gameboard[h][v + 3] = "B"
                            l = [i, h, v,0]
                            ships.append(l)
                            break

    else:
        while (True):
            v = random.randint(0, 7)
            h = random.randint(0, 1)
            if (gameboard[h][v] == False):
                if (gameboard[h + 1][v] == False):
                    if (gameboard[h + 2][v] == False):
                        if (gameboard[h + 2][v] == False):
                            gameboard[h][v] = "B" #Battleship - size 4
                            gameboard[h + 1][v] = "B"
                            gameboard[h + 2][v] = "B"
                            gameboard[h + 3][v] = "B"
                            l = [i, h, v,0]
                            ships.append(l)
                            break

    if (i == 1):
        while (True):
            v = random.randint(0, 3)
            h = random.randint(0, 4) # Aircraft Carrier - size 5
            if (gameboard[h][v] == False):
                if (gameboard[h][v + 1] == False):
                    if (gameboard[h][v + 2] == False):
                        if (gameboard[h][v + 3] == False):
                            if (gameboard[h][v + 4] == False): 
                                gameboard[h][v] = "A" 
                                gameboard[h][v + 1] = "A"
                                gameboard[h][v + 2] = "A"
                                gameboard[h][v + 3] = "A"
                                gameboard[h][v + 4] = "A"
                                l = [i, h, v,0]
                                ships.append(l)
                                break

    else:
        while (True):
            v = random.randint(0, 7) #v = vertical
            h = random.randint(0, 0) #h = horazonatal 
            if (gameboard[h][v] == False):
                if (gameboard[h + 1][v] == False):
                    if (gameboard[h + 2][v] == False):
                        if (gameboard[h + 3][v] == False):
                            if (gameboard[h + 4][v] == False):
                                gameboard[h][v] = "A"
                                gameboard[h + 1][v] = "A"
                                gameboard[h + 2][v] = "A"
                                gameboard[h + 3][v] = "A"
                                gameboard[h + 4][v] = "A"
                                l = [i, h, v,0] 
                                ships.append(l) #adss them to the list
                                break

# all of the above code is basicly the same until here, so i didnt feel the need
# to comment it, other then the ship it is.
    return ships
def inputUser(): #gets the  input of the position you want to shoot
    print("ATTACK!")
    print(" ") #spacer 
    r = int(input("Enter row number : ")) #gets the row
    c = int(input("Enter column number : ")) #gets the column
    while(r>5 or c>8):
            print("Invalid position, enter again!") #checking for valid things
            r = int(input("Enter row number : "))
            c = int(input("Enter column number : "))
           
    return([r,c]) #returns the row and column values


# checks if the ships have been hit or not
def checkHit(n,ships):
    r = n[0]-1
    c = n[1]-1
    if(gameboard[r][c]=="E") or (gameboard[r][c]=="D") or (gameboard[r][c]=="B") or (gameboard[r][c]=="A"): 
        #checking if the row or column has a letter for a ship taht has been hit
        gameboard[r][c]="H"
        print("You hit a ship!") #nice shot
    else:
        gameboard[r][c]="M"
        print("You missed the shot!") #youll get this a lot, goodluck hitting a ship!
    if(ships[0][3]==0):
        i = ships[0][0]
        if (i == 1):
            v = ships[0][2] # h = hit, M = miss
            h = ships[0][1]
            if(gameboard[h][v]=="H"):
                if(gameboard[h][v+1]=="H"):
                    print("You sunk my escort!")
                    ships[0][3]=1

        else:
            v = ships[0][2]
            h = ships[0][1]
            if (gameboard[h][v] == "H"): #if hit then and all of them have been hit, it sinks
                if (gameboard[h+1][v] == "H"):
                    print("You sunk my escort!")
                    ships[0][3] = 1

    if(ships[1][3]==0):
        i =ships[1][0]
        if (i == 1):
                v = ships[1][2]
                h = ships[1][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h][v + 1] == "H"):
                        if (gameboard[h][v + 2] == "H"):
                            print("You sunk my destroyer!")
                            ships[1][3] = 1
        else:
                v = ships[1][2]
                h = ships[1][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h + 1][v] == "H"):
                        if (gameboard[h + 2][v] == "H"):
                            print("You sunk my destroyer!")
                            ships[1][3] = 1

    if (ships[2][3] == 0):
        i = ships[2][0]
        if (i == 1):
                v = ships[2][2]
                h = ships[2][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h][v + 1] == "H"):
                        if (gameboard[h][v + 2] == "H"):
                            if (gameboard[h][v + 3] == "H"):
                                print("You sunk my battleship!")
                                ships[2][3] = 1
        else:
                v = ships[2][2]
                h = ships[2][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h + 1][v] == "H"):
                        if (gameboard[h + 2][v] == "H"):
                            if (gameboard[h + 2][v] == "H"):
                                print("You sunk my battleship!")
                                ships[2][3] = 1
    if (ships[3][3] == 0):
        i = ships[3][0]
        if (i == 1):
                v = ships[3][2]
                h = ships[3][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h][v + 1] == "H"):
                        if (gameboard[h][v + 2] == "H"):
                            if (gameboard[h][v + 3] == "H"):
                                if (gameboard[h][v + 4] == "H"):
                                    print("You sunk my aircraft carrier!")
                                    ships[3][3] = 1
        else:
                v = ships[3][2]
                h = ships[3][1]
                if (gameboard[h][v] == "H"):
                    if (gameboard[h + 1][v]== "H"):
                        if (gameboard[h + 2][v] == "H"):
                            if (gameboard[h + 3][v] == "H"):
                                if (gameboard[h + 4][v] == "H"):
                                    print("You sunk my aircraft carrier!")
                                    ships[3][3] = 1

                                    #all of that was just repeated hit or miss code, so theres not much to write about it!
                                    
                                    #just one code block for all of the diffrent ship sizes, you can tell without the sring by looking at the v and h vars

                                 # if it doesent hit any of the spots labled there with h, then it lables the shot with a M for miss
    return ships
    
    #code to be run in the main loop for the game
def main():
    #instrustions shown above the board

    print(" WELCOME TO THE GAME!")
    print(" ") #acts as a spacer between the two
    print(" HOW TO PLAY:")
    print(" 1) enter the horazontal number")
    print(" 2) enter the verticle number")
    print(" congrats you have now made a shot!")
    print("only input numerical values")
    print(" ") 
    print(" SHIPS Labled AS:")
    print(" ") 
    print(" Escort - size: 2, LABEL: E") 
    print(" Destroyer - size: 3, LABEL: D")
    print(" Battleship - size 4, LABEL: B") 
    print(" Aircraft Carrier - size 5, LABEL: A")
    print(" ") 

    ships = placeShips(gameboard) #places random ships on the board
    printGame(gameboard) #prints the bame on the gamebord
    while(True):
        #loops though, till you win or die
        r = inputUser()
        ships = checkHit(r,ships)
        printGame(gameboard)
        print(" ") 

if __name__ == '__main__':
    #runs the main
    try:
       main()
    except:
        print("loaded")
        main() # just incase something weird happens on "startup"

    # notes:

    # the position of the ships is shown so you can speedrun the game and hit them
    # its a feature and not a bug,  I intentally did it to make it easyer to see how it works
    # and if its randomized or not!

# I Should also mention that if you enter letters the game will just die intentinally, i was going to set up and except, 
## but in the intrest of time, i decided against it.