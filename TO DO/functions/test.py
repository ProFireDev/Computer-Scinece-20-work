def getNumber(Msg,Min =1, Max= 10,Type = int):
    # for int defults
    if(Type==int):
        try:
            value=int(input(Msg))
            if(value<=Max):
                if(value>=Min):
                    return value

        except ValueError:
            print("This is not a whole number.")
            try:
                value=int(input("Type a number:"))
                if(value==float):
                    try:
                        value=float(input(Msg))
                        if(value<=Max):
                            if(value>=Min):
                                return value
                    except ValueError:
                        print("This is not a Float (decimal).")
            except:
                print("This is not a proper number, please format it correctly.")

    elif(Type==float):
        try:
            value=float(input(Msg))
            if(value<=Max):
                if(value>=Min):
                    return value
                    
        except ValueError:
            print("This is not a float (decimal).")
            try:
                value=int(input("Type a number:"))
            except ValueError:
                print("This is not a float (decimal).")
