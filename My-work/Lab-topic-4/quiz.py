# Regular expressions quiz
# Author: Fatima Oliveira

import re

regex = "\["
filename = "quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")


'''
What lines will be printed out for the following regular expressions? Note that regular expressions in python are case sensitive:
a. hello - 1 line
b. Hello - 2,3 and 5 line
c. ^Hello - 2 and 3 line
d. ^Hell*o - 2, 3, 4 and 6
e. ^Hell+o - 2, 3 and 6
f. ^Hell?o - 2, 3 and 4
g. ^hello [A-Z] - Nothing
h. ^Hello [A-Z] - 3 line
i. = - 7 line
j. # -  8 line
k. [ - error, should be ("\[")
l. ^$ - line 10, empty
'''