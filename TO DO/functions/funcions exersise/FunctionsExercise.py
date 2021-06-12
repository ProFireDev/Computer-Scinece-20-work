
#1) Write a function called subNumbers that subtracts 2 numbers and returns the
#   result. Note, if given decimal numbers, it should round the result to 3 decimal
#   places. (The round() function will be useful here)
def subNumbers(num1,num2):
    output = num1 - num2
    round(output, 3)
    return output

def  isEven(Number):
    if (Number % 2) == 0:
        return(True)
    else:
      return(False)

def  isCapitalized(Word):
    if(Word.isupper()):
        return(True)
    else:
        return(False)
def  isMultiple(Number, MultipleOf):
    if (Number % MultipleOf == 0):
        return(True)
    else:
        return(False)


def Sum(UpTo, StartFrom):
    
    return

def datingRange(Age):
     lower = (Age/2)+7
     oldest =(Age-7)*2 #thats proper math right?
     return (int(lower)),((int(oldest)))