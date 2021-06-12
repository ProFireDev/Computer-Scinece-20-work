Functions and Libraries

For this assignment you will be creating the following functions in a file called **myTools**. Your code will only contain functions and will not run any code when the program is run. All of your functions should be well documented and explain how that function should be used (what the parameters are, what type they should be, what the function does, what the function returns etc.)

0) Create a function named **getNumber()** that asks the user to input a number and returns that number as an integer or floating point number, depending on what the mode is set to (default should be integer). It should have a required parameter called Msg that contains the string that will be displayed when the user is asked for input. The function must have an error catching code to protect against bad inputs. It should also have optional minimum and maximum parameters for the range the number should be in and ensure that the inputted number is within that range before returning it. Note that the function should allow for just a minimum or maximum value to be specified.

Parameters:

Min = None (optional)
Max = None (optional)
Type = Int (optional)
Msg (required)

Returns an integer or a floating point number, depending on what Type is set to.

1) Create a function named **makeChange()** that takes in a decimal number representing some amount of money and returns how many of each type of bill and coin are needed to equal that amount as a string

Parameters:

Amount

Returns a formatted string containing what amounts of each coin and bill should be given to equal the amount given.

1.1) Create another function named **getChange()** that takes in two parameters, how much a person owes and how much a person paid in cash, return what bill and and coins they should receive as change and returns it as a string. This function should call the makeChange() function to calculate what change should be given.

Hint: Use integer division (//) and modulo (%) functions to calculate how many of each denomination should be given as change

Parameters:

Owed, Paid (required)

Returns the same as getChange, but for the difference between the amount owed and the amount paid

2) Create a function called **isPrime()** that takes in an integer number as a parameter and returns True if that number is a prime number and False if it is not. Note that there are several opportunities to improve the performance of this function so that it runs faster. Without optimization, this function will be VERY slow when applied to large numbers.

Parameters:

Number (required)

Returns True or False, depending on whether number is prime or not.
