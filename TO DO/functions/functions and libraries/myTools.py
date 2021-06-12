

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


def makeChange(Amount):
      #do math to figure out bills and coins:
    try:
     Amount = () # not sure if pennys count , because they dont exist anymore, but included just in case
     for change in [0.25,0.10,0.50,0.10,5.00,10.00,20.00,50.00,100.00]:
        num = Amount/change
        Amount += (change,) * num
        Amount -= change * num
    #uhhh math is hard
  
    except:
        print("A fatal error has occoured!")
        print(f"the value entered is not a float!\n{Amount}!")

def getChange():
    return

def isPrime():
    return