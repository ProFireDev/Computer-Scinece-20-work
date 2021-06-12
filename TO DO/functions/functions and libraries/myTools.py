

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
      try:
          c=int(Amount) # c = change

          #coins
          quarters = c//0.25,
          c = c%0.25
          dimes = c//0.10,
          c = c%0.10
          nickels = c//0.05,
          c = c%0.05
          pennies = c//0.01,

          #bills
          hundred = c//100.00,
          c = c%100.00
          fifty  = c//50.00,
          c = c%50.00
          twenty = c//20.00,
          c = c%20.00
          ten  = c//10.00,
          c = c%10.00
          five  = c//5.00,
          c = c%5.00
          one  = c//1.00,
          c = c%1.00

          #printing out of the values:

          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n 0.25 {quarters}"

          results = Dvalues + "\n" + Cvalues
    
          return results
      except:
         error = input("an error has occoured counting\n are you sure you entered a string?\n try again? (Y or N)")
         if(error=="Y"):
             makeChange()
         else:
             quit()




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
