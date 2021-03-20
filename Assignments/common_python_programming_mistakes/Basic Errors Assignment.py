import random #imported for Error 5

# remember to use no try excepts

#Error 1
x = 1
print(x) #Fix this line so it prints 1

#added brackets ti make it print

#Error 2
y = "1"
z = 2
print(z+int(y))#Fix this line so it prints 3

#added brackets to convert string to int, aswell as int

#Error 3
#add a line here so that it prints "Hello World"

line = "hello world" # defigned the line varuble 
print(line)

#Error 4
Input = input("Enter what you want repeated ") #Fix this line so that it echos what the user inputted
print(Input) # note that vars should not start with a capital, but since thats how it was,
             # that is how i left it
#added Input var

#Error 5
print(random.randint(1,10)) #add a line to the very top of this file so that this line prints a random number

#imported random, fixed bracket

#Error 6

#Add a line here so that the next line prints 5
num =4
num +=1 # i could have num just = 5 and that would be the one line, but this is how it was
print(num) # in the example so i just left it and did that. | it could of been just num = 5 then print(num)

#Error 7
number = int(input("what number should I square? ")) #fix this line so that it prints the square of the input
print(number**2)

#fixed so it would take an int instead of a string, then it squares it.

#Error 8
name = input("what is your name? ")
print("hello " + name) #fix this line so that it prints hello and the users name

# added + sign to "add" them together when printing

#Error 9
playAgain = True
print(playAgain) #Fix this line so that it prints True

#the p was capitalized, undid that and it worked

#Error 10
#Fix both lines below so that it prints Hello
h = "Hello"
print(h) 

#this worked before but, I changed it slightly to make it more clear, see commit logs

#Error 10
#Fix the following lines so that it asks the user's age and then prints their input
Question = "How old are you? "
age = input(Question)
print(age)

#fixed wronf bracket and speeling mistake on question.

#Error 11
Name = "Mr Clark"
print(f"Hello {Name}") #fix this line so that it prints "Hello Mr Clark"

#converted to an f-string
#capitalized the n in Name