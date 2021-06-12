# imports the needed modules
import string
import re # Regular expressions, woo! (also known as dark magic)

with open('Bee movie Script.txt', 'r') as script_file:
    script = script_file.read()
    # Get total word count (excluding numbers & symbols)
    script = script.replace('-', ' ').replace('.', '').replace(':', ' ').replace("'", '')  # Filter out specific symbols
    symbol_instances = re.findall(r'\b[^a-zA-Z\s]\b', script)   # Regex search of all other symbols || this was so painful to write. (thanks stackoverflow)
    numbers_instances = re.findall(r'[0-9]+', script)   # Regex search of numbers with 1+ digits || this one was actually kinda simple
    count = 0 # gotta start somewhere, and it cant be 1
    for instance in symbol_instances: # checking for weird symboles ex &, #, @, ect.
        script = script.replace(instance, ' ')

    for instance in numbers_instances:
        script = script.replace(instance, ' ') # blank strings are cool...

    script = script.replace('\n', ' ')  # Replace escape character with a space
    script = re.sub(' +', ' ', script)  # Replace all extra blank spaces with only 1 space
    script_words = script.split(' ')    # Make a list of all words splitting them by a space

    for word in script_words:
        if word == '' or word == ' ':
            script_words.remove(word)   # Clean the list of any existing leftover spaces

    print(f'\n[+] Total Word Count: {len(script_words)}') #len retuns the num of items in the script_words object

    # Count unique words
    unique_words = [] # make object
    for word in script_words:
        if word not in unique_words: # if not unique then it dosent count it!
            unique_words.append(word)

    print(f'\n[+] Number of Unique Words: {len(unique_words)}') #not sure what else to comment here, len retuns the num of items
    #in the unique_words object

    # dictionary for how many times each unique word appears

    #for word in unique_words:
        #words_and_their_counts[word] = script_words.count(word)
    #print(words_and_their_counts)

    # the above code block was used for debugging to print out all of the uniqure words, to see if this was working

# Make a totally not Knockoff Script
with open('Knock Off Script.txt', 'w') as script_file:
    with open('Bee movie Script.txt', 'r') as original_script:
        knock_off_script = original_script.read()

        # Dictionary of words to replace and their replacements (can be made to accept in form of input)
        # || with modifaction, i didnt want to leave it in
        replace_dictionary = {
            'Bee': 'Flea', # haha it rymes so thats what im doing
            'Bees': 'Fleas',
            'Honey': 'sticky goodness', # I mean im not gonna say bloody goodness????
            'Nectar': 'Food',
            'Barry': 'Fleance', # it was either this or frank, creativity 100
            'Flower': 'Sandwich',
            'Flowers': 'Sandwiches', # trying not to make this horifying
            'Hive': 'Colony', # the next best thing to infestation
            'Pollen': 'Blood', # not too sure what else flees like tbh
            'Beekeeper': 'exterminator'
        }
        for key, value in replace_dictionary.items():
            knock_off_script = knock_off_script.replace(key, value) # does the replacing, woo!
            knock_off_script = knock_off_script.replace(key.lower(), value.lower()) # makes stuff lowercase

        script_file.write(knock_off_script) # does the actual writing of the 100% totally origional script
        input('\n\n[+] totally not a knockoff script written. Press Enter to End.')
        script_file.close() # closes file entirely
        original_script.close() # closes the file now that we are done and dont need it open
        quit() # exits and Quits the program

# they should add text / comment spell checkers to IDE's, im really bad at this.
# swiched over to using atom, it works way better, gonna stick with it until i can reinstall vs code

#####################################################################################################################
#                                              KNOWN ISSUES:
#
# some c's replaced  with O:
#              some of the letter C's randomly get turned into O's, I am not sure how to fix this, I think
#              It has something to do with my regular expression. (symbol_instances) my best guess for a fix
#              was doing /a but that seemed to not change anything, maybe a fix would be /c? this was hard
#              to do, so ill just leave it at that considering its not fully functional, but close. if you
#              know how to fix that, please let me know, it was very challnaging even with internet help, to
#              get it to where it is now.
#
# word count: the real script is is 13,767 words the count i get is 9207 so there was some lost, maybe in
#             titles or something? I think maybe i forgot to add unique_words and script_words together
#              because that comes out to 11,676, but that still seems too low for a good margin or error.
#
#####################################################################################################################
#                                            Final Remarks:
#
# this should be the most efficent way to do it? at the same time, it was also probbly the hardest, I dont
# recommend using regex. I dont think I will again if i can avoid it lol. do keep in mind that its about 98.7%
# functional but there is some weird edge cases that im not 100% sure how do fix. im sure its something really basic
# that im missing, but ill take the doc just to get it in, please do let me know whats up though. 
