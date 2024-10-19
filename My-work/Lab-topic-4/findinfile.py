# This is code will find some text in an access file
# Author: Fatima Oliveira

import re

regex = "\[.*\]"
filename = "smallaccess.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
            # if I did not want the [] at the beginning and end
            print(foundText[1:-1])


regex2 = ":[0-9:]{8}"
filename = "smallaccess.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex2, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
