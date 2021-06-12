

def getNumber(Msg, Min, Max, Type):
    # for int defults
    try:
     if(Type == int(Min,Max)):
        try:
         number = int(input(Msg))

        except:
            #auto catches if not an int and changes to a float
            number = float(input(Msg))
    except:
        print("improper type, please enter a float or int")
        getNumber() #reruns the function to reload it



#very much not working currently (type error)
def makeChange(Amount):
      #do math to figure out bills and coins:
    try:
     Amount = (Amount) # not sure if pennys count , because they dont exist anymore, but included just in case
     for change in [0.25,0.10,0.50,0.10,5.00,10.00,20.00,50.00,100.00]:
        num = Amount/change
        Amount += (change,) * num
        Amount -= change * num
        print(Amount) #confusing names here
    #uhhh math is hard
    except:
        print("A fatal error has occoured!")
        print(f"the value entered is not a float!\n{Amount}!")



def getChange(Owed, Paid):
    #fix code above, then just take the diffrence here
    return



# used algorithum
def isPrime(Number):
     # We know 1 is not a prime number
    if Number == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= Number:
        # Check if i divides x without leaving a remainder
        if Number % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
            
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
