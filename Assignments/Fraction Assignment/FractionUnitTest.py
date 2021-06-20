def endTest():
    print("Test Ended")
    input("Press enter to quit")
    quit()

def equalityCheck(first, second, testMsg, neg=False):
    if (first == second) ^ neg:
        print("Passed",testMsg)
        return 1
    else:
        print("Failed",testMsg)
        return 0

try:
    from fraction import *
except:
    print("Error trying to load Fraction class from file, check file name and location")
    endTest()

print("Testing Constructor function and equality operator\n")
mark = 0

try:
    half = Fraction(1,2)
    third = Fraction(1,3)
    half2 = Fraction(1,2)
    twoThird = Fraction(2,3)
    fiveSixths = Fraction(5,6)
    oneSixth = Fraction(1,6)
    threeHalf = Fraction(3,2)
    twoQuarter = Fraction(2,4)
    threeQuarter = Fraction(3,4)
    negHalf = Fraction(-1,2)
    print("Passed test of constructor Function")
    mark += 1
except:
    print("Error occured constructing fractions")
    endTest()

try:
    mark += equalityCheck(half,half2,"first equality check")
    mark += equalityCheck(half,third,"second equality check", neg = True)
except:
    print("Error occured testing for equality")
    endTest()

print("\nTesting __str__ function\n")

try:
    mark += equalityCheck(str(half),"1/2",f"{half} displayed as 1/2")
    mark += equalityCheck(str(twoThird),"2/3",f"{twoThird} displayed as 2/3")
except:
    print("Error occured testing __str__ function")

print("\nTesting operators using fractions\n")

try:
    mark += equalityCheck(half+third,fiveSixths,"Addition test: 1/2 + 1/3 = 5/6")
    mark += equalityCheck(half-third,oneSixth,"Subtraction test: 1/2 - 1/3 = 1/6")
    mark += equalityCheck(half*third,oneSixth,"Multiplication test: 1/2 * 1/3 = 1/6")
    mark += equalityCheck(half/third,threeHalf,"Division test: 1/2 / 1/3 = 3/2")
except:
    print("Error occured testing operators (+,-,*,//)")

print("\nTesting simplification function\n")

try:
    mark += equalityCheck(twoQuarter,half,"2/4 is equal to 1/2")
except:
    print("Error Testing Simplification of Fraction Constructor")

try:
    mark += equalityCheck(half+oneSixth,twoThird,"Addition test: 1/2 + 1/6 = 2/3")
    mark += equalityCheck(half-oneSixth,third,"Subtraction test: 1/2 - 1/6 = 1/3")
    mark += equalityCheck(half*twoThird,third,"Multiplication test: 1/2 * 2/3 = 1/3")
    mark += equalityCheck(threeQuarter/half,threeHalf,"Division test: 3/4 / 1/2 = 3/2")
except:
    print("Error testing simplification after operation (+,-,*,//)")

print("\nTesting toDecimal function\n")

try:
    mark += equalityCheck(half.toDecimal(),1/2,"1/2 is the same as 0.5")
    mark += equalityCheck(third.toDecimal(),1/3,"1/3 is the same as 0.3333..")
except:
    print("Error testing toDecimal function")

print("\nTesting math operations with integers\n")

try:
    mark += equalityCheck(half+1,threeHalf,"Addition test: 1/2 + 1 = 3/2")
    mark += equalityCheck(half-1,negHalf,"Subtraction test: 1/2 - 1 = -1/2")
    mark += equalityCheck(half*3,threeHalf,"Multiplication test: 1/2 * 3 = 3/2")
    mark += equalityCheck(half/3,oneSixth,"Division test: 1/2 / 3 = 1/6")
except:
    print("Error testing math operations with integers")

print(f"\nUnit Test Results: {mark}/20")
endTest()
