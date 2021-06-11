# This function tests the inputted function to see if it returns the correct answer
def unitTest(function, args, answer, testMsg):
    def passed(testMsg):
        print(f"Passed {testMsg}")
        return 1
    
    if callable(answer):
        if type(args) == tuple and answer(*args):
            return passed(testMsg)
        elif type(args) == dict and answer(**args):
            return passed(testMsg)
        elif type(args) in (float,int,str,bool,list) and answer(args):
            return passed(testMsg)
    else:
        if type(args) == tuple and function(*args) == answer:
            return passed(testMsg)
        elif type(args) == dict and function(**args) == answer:
            return passed(testMsg)
        elif type(args) in (float,int,str,bool,list) and function(args) == answer:
            return passed(testMsg)
        
    print(f"Failed {testMsg}")
    return 0

try:
    from ArraysExercise import *
except:
    print("ArraysExercise not found, check to make sure it is named correctly and is in the same folder as this program\n")

print("Testing sumList Function")
Q1 = 0

while True:
    try:
        Q1 += unitTest(sumList,[1,2,3,4],10,"sum of 1,2,3,4 = 10")
    except NameError:
        print("sumList Function not found, check if named correctly")
        break
    Q1 += unitTest(sumList,[-51,35,20,-4],0,"sum of -51,35,20,-4 = 0")

    try:
        Q1 += unitTest(sumList,{"NumList":[5]},5,"parameter name check")
    except:
        print("Failed parameter name check (NumList)")

    try:
        Q1 += unitTest(sumList,[],0,"sum of empty list = 0")
    except:
        print("Failed sum of empty list = 0")
    break

print("\nTesting makeNumList")
Q2 = 0

def Q2Test(Lower,Upper):
    j = Lower
    for i in makeNumList(Lower,Upper):
        if i != j:
            return False
        j += 1
    return j == Upper+1

while True:
    try:
        Q2 += unitTest(makeNumList,(0,10),Q2Test,"generate list from 0 to 10")
    except NameError:
        print("makeNumList Function not found, check if named correctly")
        break

    Q2 += unitTest(makeNumList,(5,20),Q2Test,"generate list from 5 to 20")

    Q2 += unitTest(makeNumList,(-10,10),Q2Test,"generate list from -10 to 10")

    try:
        makeNumList(Lower=1,Upper=5)
        print("Passed parameter name check")
        Q2 += 1
    except:
        print("Failed parameter name check (Lower,Upper)")
    break

print("\nTesting getEvens function")
Q3 = 0

def Q3Test(NumList):
    result = getEvens(NumList)
    for i in NumList:
        if i%2 == 0 and not(i in result):
            return False
        if i%2 == 1 and i in result:
            return False
    for i in result:
        if not(i in NumList):
            return False
    return True

while True:
    try:
        Q3 += unitTest(getEvens,([1,2,3,4,5,6,46,26,84,245,36]),Q3Test,"evens in [1,2,3,4,5,6,46,26,84,245,36]")
    except NameError:
        print("getEvens Function not found, check if named correctly")
        break

    Q3 += unitTest(getEvens,([1,3,5,7,893,31,785]),Q3Test,"no evens in [1,3,5,7,893,31,785]")

    try:
        getEvens(NumList=[1,2,3,4])
        Q3 += 1
        print("Passed parameter name check")
    except:
        print("Failed parameter name check (NumList)")

    try:
        Q3 += unitTest(getEvens,[],Q3Test,"empty list check")
    except:
        print("Failed empty list check")
    break

print("\nTesting countElements Function")
Q4 = 0

while True:
    try:
        Q4 += unitTest(countElements,[1,2,3],{1:1,2:1,3:1},"counting elements in [1,2,3]")
    except NameError:
        print("getEvens Function not found, check if named correctly")
        break

    Q4 += unitTest(countElements,[1,1,1,1],{1:4},"counting elements in [1,1,1,1]")
    
    Q4 += unitTest(countElements,[1,2,2,3,3,3,4,4,4,4],{1:1,2:2,3:3,4:4},"counting elements in [1,2,2,3,3,3,4,4,4,4]")

    Pass = True
    Ans = {"a":1,"b":1,"c":1}
    try:
        countElements(List=["a","b","c"])
        print("Passed parameter name check")
        Q4 += 1
    except:
        print("Failed parameter name check")
    break

print("\nTesting outerProduct")
Q5 = 0

def Q5Test(List1,List2):
    result = outerProduct(List1,List2)
    for i in range(len(List1)):
        for j in range(len(List2)):
            if result[i][j] != List1[i]*List2[j]:
                return False
    return True

while True:
    try:
        Q5 += unitTest(outerProduct,([1,2],[3,4]),Q5Test,"outer product of [1,2] and [3,4]")
    except NameError:
        print("outerProduct Function not found, check if named correctly")
        break

    Q5 += unitTest(outerProduct,([4,5,6,1,2,3,4],[7,8,9]),Q5Test,"outer product of [4,5,6,1,2,3,4] and [7,8,9]")

    Q5 += unitTest(outerProduct,([0,-2,6,3],[7,3,-6,1]),Q5Test,"outer product of [0,-2,6,3] and [7,3,-6,1]")

    try:
        outerProduct(List2=[0,1], List1=[1,0])
        Q5 +=1
        print("Passed parameter name check")
    except:
        print("Failed parameter name check (List1,List2)")
    break

print("\nFinal Results\n")
print(f"sumList function: {Q1}/4")
print(f"makeNumList function: {Q2}/4")
print(f"getEvens function: {Q3}/4")
print(f"countElements function: {Q4}/4")
print(f"outerProduct function: {Q5}/4")
print(f"Total: {Q1+Q2+Q3+Q4+Q5}/20")
