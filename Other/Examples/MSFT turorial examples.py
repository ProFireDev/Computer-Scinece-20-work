#this is kinda buggy, line 460 has an error, I just commented out the line to
#fix it temporairly

# This file contains a list of examples from the Microsoft Python for 
#Beginners series.

#follow along on this playlist here:
#https://youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6

# this looks super intimidating but its really not

#excuse the spelling too, because i am super bad at it, and they
#do not have a spell checker in IDE's for some reason

# python verson 3.9.2, remember to click install to path in the installer

# if looking for a spacific thing, they are labled by topic, so you
# can Ctrl + f to find it

# Print statements //how to print stuff to the console

print("hello world with double quotes")

print('hello world with single quotes')

# Printing outputs from varubles with imput

varExample = input("type imput here ")
print(varExample)

#Displaying blank lines in the output ex: (lazy)

print("hello world with blanks 1")
print() #This is the lazy way for a blank line
print("above is the blank line")

# The proper way to print on a new line with /n

print("blank line with \n a split, to split the middle of the string")

# Printing is helpful for log files and debugging

#you can use a multi line long string to have comments on more then one line

#Using strings

this_is_a_varuble = 'some text in a string'
print(this_is_a_varuble) # prints whats on the line above

# combineing strings
string_One ='this is the first string of text'
string_Two =' this is the second string of text'
print(string_One+string_Two) # "adding" the two strings together to combine them

# Adding new strings with the two strings
print('more text' + string_One + string_Two)
print('more text ' + string_One + ' ' + string_Two) # you can also add spaces

#Modifying strings

sentence = 'this is a test sentince'

print(sentence.upper()) # converts sentence to uppercase
print(sentence.lower()) #converts sentence to lowercase
print(sentence.capitalize()) #capitalizes the sentince
print(sentence.count('a')) #returns string lenth

#You can combine more then one string formatter ex

first_name = input('enter first name here ')
last_name = input('enter last name here ')
print('hello ' + first_name.capitalize() + ' ' \
    + last_name.capitalize())
    
#Formatting strings properly

#Generic messy format
output = 'hello, ' + first_name + ' ' + last_name

#Passing peramiters through to strings
output = 'hello, {} {}'.format(first_name, last_name)

# Another way of passing things though witgh an array (counting starts with 0)
output = 'hello, {0} {1}'.format(first_name, last_name)

# In python 3, you can format inside of the string
output = f'hello, {first_name} {last_name}'

# Numerical data types eg floats and numbers

#ex

pi = 3.14159
print(pi)

#doing math

# + addition, - subtraction, * multiplication, / is division, ** exponent / example

num1 = 6
num2 = 2

# adding the numbers
print(num1 + num2)

#raising to a power (exponent)
print(num1 ** num2)

#combineing data types

# type converson
days_in_feb = 28
print(str(days_in_feb) + 'days in february')

#converting strings to numbers

first_num =input('enter a number ')
second_num =input('enter a number ')
print(first_num + second_num)

# type converson for ints and floats from strings

print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

# if statements and conditional logic

price = input('enter price value here, in float form ')
price = float(price)

if price >= 1.00: # there is always a colen at the end of a condition
    tax = .07
    print(tax)

# operation symbols: > is greater than, < is less than
# >= is greater than equal to, <= is less than equal to
# == is equal to and != is not equal to

# if else statements:

if price >= 1.00: # there is always a colen at the end of a condition
    tax = .07
else: # if the condition is not met, then do this under the else statement
    tax = 0
    print(tax)

#comeparing strings

#string compareisons are case sensitive

country = 'CANADA'
if country.lower() == 'canada':
    print('oh look a Canadian ')
else:
    print('rip you are not a Canadian')

#Handeling Multipule conditions elif statements

#basic elif

province = "null"

if province == 'AB':
    tax = 0.05
elif province == 'nv':
    tax =0.05
elif province == 'on':
    tax = 0.13

#elif with else statements

if province == 'AB':
    tax = 0.05
elif province == 'nv':
    tax =0.05
elif province == 'on':
    tax = 0.13
else:
    tax = 0.15

#if with elif with or and else statement

# \ can be used to break a singe line of code into two lines

if province == 'AB'\
    or province == 'nv':
    tax =0.05
elif province == 'on':
    tax = 0.13
else:
    tax = 0.15

#checking a list of values, with in operator

if province in('AB','NV','YK'):
    tax = 0.05
elif province == 'ON':
    tax = 0.13
else:
    tax = 0.15

#Checking value with a combanation of conditions

#(Putting if statements inside eachother)

#Nesting if statements || its a good idea to put this in a function for formatting

if country == 'canada':
    if province in('AB','NV','YK'):
        tax = 0.05
elif province == 'ON':
    tax = 0.13
else:
    tax = 0.0

#Complex conditions

#Using and statements 

#Lazy way of nesting ifs

gpa = .90
lowest_grade = .75

if gpa >= .85:
    if lowest_grade >-.70:
        print('welldone')

#both conditions must be true, in order to produce true, if one or more is false, then its false
if gpa >= .85 and lowest_grade >= .70:
    print('well done, you did it the proper way')

#Complicated ifs

# boolean statements

honour_roll = False

if gpa >= .90 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

#another place in the code somewhere
if honour_roll:
    print('Well done')

#loops

#for loops

for variable in ['first item', 'second item']:
    print(variable)

# range counts the number of items in a array

for index in range(0, 2):
    print(index)

print(' ') # this is a space to seperate the numbers, ignore

#better example of how this works

for index in range(0, 8):
    print(index)

#looping with a condition (while loops)

#while loop

variable = ['item one,' 'item two in the array']
index=0 # this is where it starts counting

while index < len(variable):
    print(variable[index])
    # change the condition here so no infinate loop
    index = index + 1

#Note above is not the best example, for loops are better for that aplication

# lists, arrays and dictonary data colection types

#Lists

# lists can store any data type and can be mixed data types

names = ['first item on the list, ' 'second item on the list']
scores = []
scores.append(98) # adds a new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # collections are zero-indexed
 # the number in the block refurts to the numbered item on the list (second item on the list) in this case

#arrays

# a colection of numbers 

from array import array # need to create array object, and import it from a library
scores = array('d') # the numeric data type being used (double)
scores.append(97)
scores.append(98)
print(scores)
print(scores[1]) #  the number in the block refurts to the numbered item on the list (98) in this case
 
 #array is only one numaric data type, and only numbers

 #common list operations

names = ['susan', 'christopher']
print(len(names)) # gets the number of items or the lenth
names.insert(0, 'bill') # insets a new item before the index the 0 specifys the index the new items position in front of
print(names)
names.sort() # sorts the list in aplabetical order or inm numbers its put in smallest to largest
print(names) # prints new sorted and mondifyed list

#grabing ranges of lists

names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3] # the numbers in the box are the start and and end index. (range of the list)

print(names)
print(presenters)

#Dictionaries

#uses key value pears to find stuff

##          key       "value"
person = {'first': 'Christopher'}
person['last'] = 'Harrison' # this is the index, so you can add to the Dictionary
print(person)
print(person['first'])

#note the storage order is not guaranteed

#Dictionaries allow you to name things

#functions

#not a funtion but useful:

import datetime
#prints timesteps so yoy can see how long each section takes to run
first_name = 'Susan'
print('task completed')
print(datetime.datetime.now()) # gets the date and time and then prints it
print()

for x in range(0, 10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()

# doing this with funtions to make it look prittyer

def print_time(): # you use def to define a function
    print('task completed') 
    print(datetime.datetime.now())
    print()

first_name = 'A_Name'
print_time() #calling the funtion that was just defined

for x in range(0, 10):
    print(x)
print_time() # same idea as in js, just without the ;

#passing in peramaters

#prints the current time and task name
def print_time_peram(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'name_here'
print_time() # this is where you pass in the (peramiters)
for x in range(0, 10):
    print(x)
print_time()

# passing in to get an initial example

def get_initial(name):
    intial = name[0:1] #using a mini array to store the initial
    return intial #returns the initials value

first_name = input('enther your first name: ') #takes input from a console
first_name_init = get_initial(first_name)

#same prosess as last name
last_name = input('enter your last name: ')
last_name_init = get_initial(last_name) #passing value through()
#                                    this slash breaks one line into two lines
print('your initials are: ' + first_name_init \
    + last_name_init) #it fits on half a screen and is more readable this way

# getting creative with functions

def get_initial(name):
    intial = name[0:1] 
    return intial #returns the initials value

#takeing input again
first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

# takes first and last name, passes them here and then outputs it via a function
print('your initials are: ' \
    + get_initial(first_name) \
        + get_initial(last_name))

# remember that python works top down, so the function needs to be 
#decalred before you call it somewhere in your code

#use discriptive names too

# function perameters (advanced funtions)

def get_initial(name):
    initial = name[0:1].upper() # defining the function
    return initial

#only convert things in certin places

# basic:
first_name = input('enter your first name: ')
first_name_init = get_initial(first_name)

print('your initial is: ' + first_name_init)

#modifyed for certin peramiters only:

def get_initial_multi(name, force_uppercase):
    if force_uppercase:
        init = name[0:1].upper() #takes mame and capitalizes it
    else:
        init = name[0:1] #only isolates the first letter
    return init

first_name = input('enter yout first name here: ')
first_name_init = get_initial_multi(first_name, False) #passing perams though
    
# they need to be passed though in the order they are declared

print('your initial is: ' + first_name_init)

# setting defult values for perameters

def get_init(name, force_uppercase=True): #setting a defult value here
    if force_uppercase: #        so there doesent need to be one below
        init = name[0:1].upper()
    else:
        init = name[0:1]
    return init

first_name = input('enter yout first name here: ')
#first_name_init = get_initial_multi(force_uppercase,first_name) 
#  broke it lol
# #no need to pass val, cuz defult is true

print('your initial is: ' + first_name_init)

#named notation

#when using named perameters you can specify perams in any order needed / wanted

def get_init_named_notation(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('enter yout first name here: ')
first_name_init = get_init_named_notation(force_uppercase=True, \
    name = first_name) #when this is called you set the values in the function

print('your initial is: ' + first_name_init)

#good example of how to use this properly

#ignore values, they are place holders

error_code = 45
error_severity = 1
log_tpo_db = True
error_message ='error 501 (not implemented)'
source_module ='my_math_method'

def error_logger(error_code, error_severity, log_tpo_db, \
    error_message, source_module):

    print('there is an error: ' + error_message)

#some code here that would log to a database or a file

first_number = 10
second_number = 5

if first_number > second_number:
    error_logger(error_code=45, error_severity=1,
    log_tpo_db=True,
    error_message='second number is greater then the first',
    source_module='my_math_method')

# makes it way easyer to understand when reading / debugging, because its named
# think about maintaining and documenting the code for other people to read & understand

#Modules and packages

#creating modules

#this is now a module

#file name of the modual
message ='this is a string'

def display(message, is_warning=False):
    if is_warning:
        print('warning!!')
    print(message)
# this is now a new module

#import mod as namespace

#import the file name ex module.py

#not much i can do here so take a look at this:
#https://youtu.be/Uei2ILcxuPs?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&t=135

#import* means import everythng globaly

#packages

#google it, or search the python package index

#requirements.txt
#put all of the pacages in a list in this file

#error handling / debugging

#https://youtu.be/HQqqNBZosn8?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&t=64

# catching runtime errors

#assining value for demo
y= 0

try:
    print(x / y)
except ZeroDivisionError as e: # not looking for a peramiter, so it catches and accepts what happens
        #log e somewhere
    print('somthing went wrong')
except:
    print('something went really wrong')
finally:
    print('this runs no matter what happens')

#watch out for logic errors too
#take a look at the stack trace in the debugger, 
# that will show you all of the calls that have been made