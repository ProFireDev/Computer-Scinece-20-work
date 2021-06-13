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