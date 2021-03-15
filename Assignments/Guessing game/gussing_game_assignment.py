import random

#note changed var didWin in the example to win

#score keeping vars
wins = 0
gamesPlayed = 0


while True:
    #setup Phase
    while True:
        try:
            diff = int(input("choose your difficulty (1-3)\n")) # error catching, for imput protection
        except:
            print('thats not a valid input')
            continue
        break
    
    upperLimit = diff*10 ### possable bug, look into this ###
    number = random.randint(1,upperLimit)
    win=False

    #print(number) #test shows the number being generated

    print(f"I'm thinking of a number between 1 and {upperLimit}")
    # this is the inner game loop
    for i in range(3): 
        #main loop
        while True: #more type protection to varify inputs
            try:
                 guess = int(input('what number am I thinking of?\n')) # gets imput converts to a int
            except:
                print("that's not a valid input")
                continue
            break

        if number == guess:
            #win section
            print('thats correct!')
            win=True
            wins += 1
            gamesPlayed += 1
            break
        print('sorry, that is incorrect')
    if not win:
        #loose section
        gamesPlayed += 1
        print(f'the correct number was {number}')
        #display score
        print(f'you have won {wins} out of {gamesPlayed}')

    #play again section
    play_Again = input('do you want to play again y/n \n').lower()
    if play_Again == 'y' or play_Again == 'yes':
        continue #loops back around to the beginning of the program
    else:
        print('goodbye')
        break