import random

gameboard = [[False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False],
             [False,False,False,False,False,False,False,False]]

def printGame(gameboard):
    print("  1 2 3 4 5 6 7 8")
    counter = 1
    for i in gameboard:
        print(str(counter)+"",end=" ")
        for j in i:
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
        print()

def placeShips(gameboard):
    ships = []
    i = random.randint(1,2)
    if(i==1):
        v = random.randint(0,6)
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
        ships.append(l)
    i = random.randint(1,2)
    if(i==1):
        while(True):
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
    else:
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
            v = random.randint(0, 4)
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
                            gameboard[h][v] = "B"
                            gameboard[h + 1][v] = "B"
                            gameboard[h + 2][v] = "B"
                            gameboard[h + 3][v] = "B"
                            l = [i, h, v,0]
                            ships.append(l)
                            break
    if (i == 1):
        while (True):
            v = random.randint(0, 3)
            h = random.randint(0, 4)
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
            v = random.randint(0, 7)
            h = random.randint(0, 0)
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
                                ships.append(l)
                                break
    return ships
def inputUser():
    print("ATTACK!")
    r = int(input("Enter row number : "))
    c = int(input("Enter column number : "))
    while(r>5 or c>8):
            print("Invalid position, enter again!")
            r = int(input("Enter row number : "))
            c = int(input("Enter column number : "))
    return([r,c])

def checkHit(n,ships):
    r = n[0]-1
    c = n[1]-1
    if(gameboard[r][c]=="E") or (gameboard[r][c]=="D") or (gameboard[r][c]=="B") or (gameboard[r][c]=="A"):
        gameboard[r][c]="H"
        print("You hit a ship!")
    else:
        gameboard[r][c]="M"
        print("You missed the shot!")
    if(ships[0][3]==0):
        i = ships[0][0]
        if (i == 1):
            v = ships[0][2]
            h = ships[0][1]
            if(gameboard[h][v]=="H"):
                if(gameboard[h][v+1]=="H"):
                    print("You sunk my escort!")
                    ships[0][3]=1
        else:
            v = ships[0][2]
            h = ships[0][1]
            if (gameboard[h][v] == "H"):
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
    return ships
def main():
    print("WELCOME TO THE GAME")
    ships = placeShips(gameboard)
    printGame(gameboard)
    while(True):
        r = inputUser()
        ships = checkHit(r,ships)
        printGame(gameboard)
        print()
if __name__ == '__main__':
    main()