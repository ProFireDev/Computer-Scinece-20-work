def sumList(NumList):
   # Takes in a list of numbers and returns the sum of those numbers.
   # Note: Standard function sum(x) does the same thing and more
    s = 0
    for x in NumList:
        s += x
    return s

def makeNumList(Lower, Upper):
    # Takes in two integers and returns a list containing every number starting from first and ending at the second, including both end points.
    return [x for x in range(Lower,Upper+1)]

def getEvens(NumList):
    # Takes in a list of integers and returns a list containing every even number in the original list
    return [x for x in NumList if x % 2 == 0]

def countElements(List):
    # Takes in a list and returns a dictionary with the elements of the inputted list being the keys and the number of times that element was in the list being the value.
    d = dict()
    for x in List:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d

def outerProduct(List1, List2):
    # Takes in two lists of numbers and returns a 2D list such that the number at position [i][j] is equal to the ith element of the first list times the jth element of the second list.
    return [ [i*j for j in List2] for i in List1]

# This was really simple to make, I domt know what else to comment on, other then there might be a more efficent way to do this, however im not sure what it would be

# one thing i would fix to make this more human readable is to not just use letters, i would chuck some real names in there, but this works.
# I kinda like it to be more logical this way, because i can kinda think of it like algeba 
