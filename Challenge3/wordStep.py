# Had to download file and put in folder but split is from assignment
wordfile = open("unixWords.txt")
words = wordfile.read().upper().split()


#Get all words that are one letter more and are annagrams
def AllSteps(base):
    newWords = []
    oneOff = False # define
    for word in words:
        if(len(word) == len(base)+1):
            oneOff = False
            wordList = list(base.upper())
            for letter in word:
                if not letter in wordList:
                    if(oneOff == True):
                        oneOff = False
                        break
                    else:
                        oneOff = True
                else:
                    wordList.pop(wordList.index(letter))
            if(oneOff == True):
                newWords.append(word)
    return newWords

# First test is match
print(AllSteps("APPLE"))