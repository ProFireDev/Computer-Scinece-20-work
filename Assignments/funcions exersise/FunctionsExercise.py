# 1) Write a function called subNumbers that subtracts 2 numbers and returns the
#    result. Note, if given decimal numbers, it should round the result to 3 decimal
#    places. (The round() function will be useful here)
#
# Parameters: Num1,Num2
#
# Output: a number

# Function 1

def subNumbers (Num1, Num2):
    Number = round (Num1 - Num2, 3) #rounds to 3 decimal places
    return Number


# 2) Write a function called isEven that checks if a number is even. (the modulo
#   (%) operator will be useful here)
#
# Parameters: Number
#
# Output: True/False

# Function 2:

def isEven(Number): 
    if Number % 2 == 0: 
        return(True)
    else:
        return(False)

#if remainder is even, its even

# 3) Write a function called isCapitalized that checks if a word is capitalized. 
#    (String operations and methods will be useful here)
#
# Parameters: Word
#
# Output: True/False

# Function 3

def isCapitalized (Word):
    if(Word[0].isupper()): #checks if uppercase 
        return True
    else: 
        return False #if not, returns false


# 4) Write a function called isMultiple that checks if the first number is a multiple 
#    of the second number. (Modulo will be applicable here too)
#
# Parameters: Number, MultipleOf
#
# Outputs: True/False

# Function 4

def isMultiple (Number, MultipleOf):
    if Number % MultipleOf == 0: 
        return(True)
    else:
        return(False)


# 5) Write a function called Sum that adds together every number from the second 
#    parameter to the first parameter. The second parameter should be optional and 
#    default to 1. (I recommend using a For loop for this)
#
# Parameter: UpTo, StartFrom (optional)
#
# Output: a number

# Function 5

def Sum (UpTo, StartFrom = 1):
    result = 0
    UpTo = UpTo + 1
    for i in range (StartFrom, UpTo):
        result = result + i
    return result # retuns the sum after addition


# 6) Write a function called datingRange that takes in the person’s age and returns the youngest
#    and oldest ages the user should consider dating based on the old rule of “Half your age plus 
#    seven” for the youngest. (use your algebra skills to solve for the oldest)
#
# Parameter: Age
#
# Output: lower and upper ages as integers (In that order)

# Function 6

def datingRange(Age):

    lower = (Age / 2) + 7
    upper = (Age - 7) * 2
    return (int(lower)),(int(upper)) #returns ages
