# Had to download file and put in folder but split is from assignment
# wordfile = open("unixWords.txt")
# words = wordfile.read().upper().split()
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

def AllSteps(wordIn):
    WordSteps = []
    wordIn = wordIn.upper()
    # Get all words that are one letter more
    for word in words:
        if(len(word) == len(wordIn) + 1):
            # Itterate through a copy of the base word
            wordInCopy = wordIn
            for letter in word:
                if letter in wordInCopy:
                    wordInCopy = wordInCopy.replace(letter, "", 1) # Third param says to replace one instance of it.
            #If you can remove all the letters with a word 1 greater than it is a step
            if len(wordInCopy) == 0:
                WordSteps.append(word)

    return WordSteps

print(AllSteps("Apple"))