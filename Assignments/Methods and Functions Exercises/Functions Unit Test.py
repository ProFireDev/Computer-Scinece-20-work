try:
    from FunctionsExercise import *
except:
    print("FunctionsExercise not found, check to make sure it is named correctly and is in the same folder as this program")

print("\nTesting subNumber Function")
Q1 = 0
while True:
    
    try:
        if subNumbers(3,1) == 2:
            print("Passed 3-1=2")
            Q1 +=1
        else:
            print("Failed 3-1=2")
    except NameError:
        print("Cannot find subNumbers function, check function name")
        break
    
    if subNumbers(5.4,2.3) == 3.1:
        print("Passed 5.4-2.3=3.1")
        Q1+=1
    else:
        print("Failed 5.4-2.3=3.1")

    try:
        if subNumbers(Num2=5,Num1=3) == -2:
            print("Passed parameter name check")
            Q1+=1
        else:
            print("Failed parameter name check (Num1,Num2)")
    except:
        print("Failed parameter name check (Num1,Num2)")

    break

print("\nTesting isEven function")

Q2 = 0

while True:
    try:
        if isEven(4) == True:
            print("Passed 4 is even")
            Q2+=1
        else:
            print("Failed 4 is even")
    except NameError:
        print("Cannot find isEven function, check function name")
        break
    
    if isEven(3) == False:
        print("Passed 3 is not even")
        Q2+=1
    else:
        print("Failed 3 is not even")

    if isEven(4.5) == False:
        print("Passed 4.5 is not even")
        Q2+=1
    else:
        print("Failed 4.5 is not even")

    try:
        if isEven(Number = 0) == True:
            print("Passed parameter name check")
            Q2+=1
        else:
            print("Failed parameter name check (Number)")
    except:
        print("Failed parameter name check (Number)")
    break
    

print("\nTesting isCapitalized function")

Q3 = 0
while True:
    try:
        if isCapitalized("hello") == False:
            print("Passed 'hello' isn't capitalized")
            Q3+=1
        else:
            print("Failed 'hello' isn't capitalized")
    except NameError:
        print("Cannot find isCapitalized function, check function name")
        break

    if isCapitalized("Hello") == True:
            print("Passed 'Hello' is capitalized")
            Q3+=1
    else:
        print("Failed 'Hello' is capitalized")

    if isCapitalized("3") == False:
        print("Passed '3' isn't capitalized")
        Q3+=1
    else:
        print("Failed '3' isn't capitalized")
            
    if isCapitalized("!") == False:
        print("Passed '!' isn't capitalized")
        Q3+=1
    else:
        print("Failed '!' isn't capitalized")
    try:
        if isCapitalized(Word = "Word") == True:
            print("Passed parameter name check")
            Q3+=1
        else:
            print("Failed parameter name check (Word)")
    except:
        print("Failed parameter name check (Word)")

    break


print("\nTesting isMultiple function")
Q4 = 0

while True:
    try:
        if isMultiple(10,2) == True:
            print("Passed 10 is a multiple of 2")
            Q4+=1
        else:
            print("Failed 10 is a multiple of 2")
    except NameError:
        print("Cannot find isMultiple function, check function name")
        break

    if isMultiple(11,3) == False:
        print("Passed 11 is not a multiple of 3")
        Q4+=1
    else:
        print("Failed 11 is not a multiple of 3")

    try:
        if isMultiple(MultipleOf = 5, Number = 15) == True:
            print("Passed parameter name check")
            Q4+=1
        else:
            print("Failed parameter name check (Number,MultipleOf)")
    except:
        print("Failed parameter name check (Number,MultipleOf)")
    break

print("\nTesting Sum function")
Q5 = 0
while True:
    try:
        if Sum(3,1) == 6:
            print("Passed sum from 1 to 3 is 6")
            Q5 +=1
        else:
            print("Passed sum from 1 to 3 is 6")
    except NameError:
        print("Cannot find Sum function, check function name")
        break

    if Sum(6,3) == 18:
        print("Passed sum from 3 to 6 is 18")
        Q5 += 1
    else:
        print("Failed sum from 3 to 6 is 18")

    try:
        if Sum(5) == 15:
            print("Passed optional parameter test")
            Q5 += 1
        else:
            print("Failed optional parameter test (lower limit default to 1)")
    except:
        print("Failed optional parameter test (lower limit default to 1)")

    try:
        if Sum(StartFrom = 10, UpTo = 13) == 46:
            print("Passed parameter name check")
            Q5 +=1
        else:
            print("Failed parameter name check (UpTo,StartFrom)")
    except:
        print("Failed parameter name check (UpTo,StartFrom)")

    break

print("\nTesting datingRange function")
Q6 = 0

while True:
    try:
        if datingRange(14) == (14,14):
            print("Passed dating range for age 14 (14-14)")
            Q6+=1
        else:
            print("Failed dating range for age 14 (14-14)")
    except NameError:
        print("Cannot find datingRange function, check function name")
        break

    if datingRange(20) == (17,26):
        print("Passed dating range for age 20 (17-26)")
        Q6+=1
    else:
        print("Passed dating range for age 20 (17-26)")

    try:
        if datingRange(Age = 30) == (22,46):
            print("Passed parameter name check")
            Q6 += 1
        else:
            print("Failed parameter name check (Age)")
    except:
        print("Failed parameter name check (Age)")

    break

print("\nFinal Results\n")
print(f"subNumbers function: {Q1}/3")
print(f"isEven function: {Q2}/4")
print(f"isCapitalized function: {Q3}/5")
print(f"isMultiple function: {Q4}/3")
print(f"Sum function: {Q5}/4")
print(f"datingRange function: {Q6}/3")
print(f"Total: {Q1+Q2+Q3+Q4+Q5+Q6}/22")
    
