import random
#Initialization

wins = 0
gamesPlayed = 0

while True:
    #setup before game
    while True:
        try:
            diff = int(input("Choose a difficulty (1-3)\n"))
        except ValueError:
            print("That's not a valid input")
            continue
        break

    
    upperLimit = diff*10

    
    number = random.randint(1,upperLimit)
    didWin = False
    print(f"I'm thinking of a number between 1 and {upperLimit}")
    #main game loop
    for i in range(3):
        
        guess = int(input("What number am I thinking of?\n"))

        if number == guess:
            #win section
            print("That's correct!")
            didWin = True
            wins += 1
            gamesPlayed += 1
            break

        else:
            print("Nope, that's not it")
            
    #end of game section
            
    if not didWin:
        #lose section
        gamesPlayed += 1
        print(f"The correct number was {number}")

    #display score
    print(f"You have won {wins} games out of {gamesPlayed}")
    
    #play again   
    playAgain = input("Do you want to play again? (y/n)\n").lower()
    if playAgain == "y" or playAgain == "yes":
        continue
    else:
        print("Goodbye!")
        break
