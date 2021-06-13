# import the modules
import math

# asks the user to input a number and returns that number as an integer or floating 
# point number, depending on what the mode is set to (default should be integer). 
# It should have a required parameter called Msg that contains the string that will be 
# displayed when the user is asked for input. The function must have an error catching code to protect 
# against bad inputs. It should also have optional minimum and maximum parameters for the range the 
# number should be in and ensure that the inputted number is within that range before returning it. 
# Note that the function should allow for just a minimum or maximum value to be specified.
#
#Parameters:

#Max = None (optional)
#Type = Int (optional)
#Msg (required)

#Returns an integer or a floating point number, depending on what Type is set to.


def getNumber(Msg,Min =1, Max= 10,Type = int):
    # ^define the perams
    # for int defults
    if(Type==int):
        try:
            # trys to get an inital input
            value=int(input(Msg))
            # checks for max val or if equal
            if(value<=Max):
                # checks to see if numver is above minimum value
                if(value>=Min):
                    return value
                    
                    # value error exceptions for imput is not a number or the right number
                    # according to the type
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
                            # checks if a float was entered instead as a way to catch that
                    except ValueError:
                        print("This is not a Float (decimal).")
            except:
                print("This is not a proper number, please format it correctly.")
                # if its not the defult value, then it auto assumes its a float and treats it accordingly
    elif(Type==float):
        try: # does all the same things as before, just as a float
            value=float(input(Msg))
            if(value<=Max):
                if(value>=Min):
                    return value
                    
        except ValueError:
            print("This is not a float (decimal).")
            try:
                value=int(input("Type a number:"))
            except ValueError:
                print("This is not a float (decimal).") # more type checking, to make sure you cant just use a string



#takes in a decimal number representing some amount of money and returns how many of each 
# type of bill and coin are needed to equal that amount as a string

# Parameters:

# Amount 

# Returns a formatted string containing what amounts of each coin and bill should 
# be given to equal the amount given.

#lets make some change!
def makeChange(Amount):
      try:
          NewAmount =math.modf(Amount) # takes the ammount, makes a tuple so that the int and then float can be
          # prosessed seprarely
          # float 0, int 1
          b=int(Amount[1]) # b = bills 
            # bills
          hundred = b//100.00
          b = b%100.00
          fifty  = b//50.00
          b = b%50.00
          twenty = b//20.00
          b = b%20.00
          ten  = b//10.00
          b = b%10.00
          five  = b//5.00
          b = b%5.00
          one  = b//1.00
          b = b%1.00
          # all of the above are the diffrent demomanations of bills that it checks for
          
          # coins
          c=float(NewAmount[0])
          quarters = c// 0.25
          c = c%0.25
          dimes = c//0.10
          c = c%0.10
          nickels = c//0.05 
          c = c%0.05
          pennies = c//0.01
          c =c%0.05

          # all of the above are the diffrent demomanations of bills that it checks for
          # printing out of the values:

          # takes all of the bill values, lables them and then gets ready to output them
          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n $0.25: {quarters}"
          # this one does the same thing for the coins
          
          # adds them together seprately
          results = Dvalues + "\n" + Cvalues
          # puts them into one final string

           #this could of all been done on one line or in one varm, but this seemed more human readable to me
          return results

      except:
         error = input("an error has occoured counting\n are you sure you entered a value?\n try again? (Y or N)")
         # some more basic error counting to make sure that its money being entered
         if(error=="Y"):
             try:
              makeChange() # trys to run the function again from the beginning.
             except:
                 print("exit code 1, a fatal error has occurred")
                 # something went wrong, so it exits and quits
                 quit()


#takes in two parameters, how much a person owes and how much a person paid in cash,
#  return what bill and and coins they should receive as change and returns it as a string. 
# This function should call the makeChange() function to calculate what change should be given.

#Hint: Use integer division (//) and modulo (%) functions to calculate how many of each 
# denomination should be given as change

#Parameters:

#Owed, Paid (required)

#Returns the same as getChange, but for the difference between the amount owed and 
# the amount paid


def getChange(Owed, Paid):
    try:
        # finds the total owed by taking how much was paid and them subtracting the cost of goods, assumes
        # that either both are the same (IE 0 money to pay out) or that the customer over paid and thats why you
        # need to pay out change

          TOTALOWED = Paid-Owed
          NewAmount =math.modf(TOTALOWED)
          # dec first, doller second
          b=int(Paid[1]) # b = bills
            # bills
          hundred = b//100.00
          b = b% 100.00
          fifty  = b//50.00
          b = b%50.00
          twenty = b//20.00
          b = b%20.00
          ten  = b//10.00
          b = b%10.00
          five  = b//5.00
          b = b%5.00
          one  = b//1.00
          b = b%1.00

          # coins
          c=float(NewAmount[0])
          quarters = c// 0.25
          c = c%0.25
          dimes = c//0.10
          c = c%0.10
          nickels = c//0.05 
          c = c%0.05
          pennies = c//0.01
          c =c%0.05
          # this part is all basicly the same as before (for the most part)
          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n $0.25: {quarters}"
          # this is the exact same as before too
          changegiven = Dvalues + "\n" + Cvalues
          # just changed the names here
          return "we Owe you ${TOTALTOTALOWED}\n" + changegiven #show the math from before and then the print out of what bills /coins 
          # are needed to pay the customer out

    except:
       error = input("an error has occoured counting\n are you sure you entered a string?\n try again? (Y or N)")
    if(error=="Y"):
        #more checking to make sure that this is extra safe, especially since this deals with money.
     try:
       getChange() #incase of failure, trys to re run it again
     except:
      print("exit code 1, a fatal error has occurred") #if it fails then it will exit and quit.
      quit()


#takes in an integer number as a parameter and returns True if that number is a 
# prime number and False if it is not. Note that there are several opportunities to 
# improve the performance of this function so that it runs faster. Without optimization, 
# this function will be VERY slow when applied to large numbers.

#Parameters:

#Number (required)

#Returns True or False, depending on whether number is prime or not.


#returns if true or false or not, baised on if the number is prime
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