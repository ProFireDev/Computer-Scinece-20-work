
file = open(r"fileREAD.txt", "r") #only works if the desired file is in the same folder
file2 =open(r"fileWrite.txt", "w") #only works if the desired file is in the same folder
#r string is a raw string it stops pyton from doing any special chericter editing

file2.write(file.read())
print(file.read()) # reads out the entire file

print(file.readline()) # reads first line or the line passed into it

#for line in file:
#   i =+ 1
#    if i == 10:
#        break
#   print(line)

file.close() # closes the file - if not closed it could create corruption problems
file2.close()