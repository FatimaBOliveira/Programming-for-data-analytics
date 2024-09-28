# Program that reads csv file.
# Author: Fatima Oliveira

# 2. Write a program to read in the data and output each line as a list. 
import csv
FILENAME= "data.csv"
DATADIR = "./csv/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)

# This result is data printed as strings.



# 3. Modify the program to deal with the header line separately

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # first row in header row
            print (f"{line}\n-------------------")
        else: # all subsequent rows
            print (line)
        linecount += 1



# 4. Modify the program to calculate the average age, there are a few ways to solve this;

    # 4a. Convert the string that is read into an integer

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row in header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # why 1-> because "age" is in column 1.
        linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1 ?

    # 4b. b. Use the quote parameter to read in the numbers as floats

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row in header row
            pass
        else: # all subsequent rows
            total += line[1] # why 1
        linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1 ?


# 5. The CVS file could of course have been read in as a Dictionary object Using DictReader().

# some code is deleted from here
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print (line)
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time? -> because it was located the line["age"] and not the position of the line with linecount.
