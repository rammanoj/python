import webbrowser
# through web browser package it is possible to open a webbroser through python code 

import sys , pyperclip

# the things copied are stored in temporarly in clip board which can be accessed by pyperclip

if(len(sys.argv)>1):

# sys.argv returns all the commandline arguments given while running the code
# in sys.argv the first argument is file path and the other are arguments given 

    word = ' '.join(sys.argv[1:])

#the above code inserts the word which you give as commandline argument as string in variable word
else:
    
    word = pyperclip.paste()

var x = input('Enter a number: ')
var y = input('Enter another number: ')
print(int(x) + int(y))

#the above line satisfies the desire to do math while the page loads
address = webbrowser.open('https://www.google.co.in/search?site=&source=hp&q=' + word)

#finally the above line opens the webbrowser and searches the word in google which is passed as command line argument
