import re
import csv

hypens = []

inventoryFound = []

allAssestsFound = []

assestsExist = []

internalAssets = r"C:\Users\htukuru\OneDrive - Alithya\Documents\myQualysData1.csv"

allAsessts = r"C:\Users\htukuru\Downloads\AI_Asset_List_athya9ht_20221122.csv"

with open(internalAssets, 'r') as file:
    myReader = csv.reader(file)
    for read in myReader:
        # print(read[1])
        # print(read)
        # newRead = re.search(r"(\w+)(\.)", read)
        # print(newRead.group(1))
        readMe = re.search(r"([\w+-]+)", read[1])
        firstGroup = readMe.group()
        inventoryFound.append(firstGroup)
        # print(firstGroup)

    print("End of the Master Inventory data")
    print("##################################################################################")

    with open(allAsessts, "r") as asstFile:
        allAssestReader = csv.reader(asstFile)

        for newRead in allAssestReader:
            allassetsSearch = re.search(r"([\w+-]+)", newRead[2])
            allassestResult = allassetsSearch.group()
            allAssestsFound.append(allassestResult)

            # print(allassestResult)

    for check in inventoryFound and allAssestsFound:
        if check in inventoryFound and allAssestsFound:
            print(check)
        # for checknow in allAssestsFound:
        #     if check in inventoryFound and
        #print(check)
        # if check in firstGroup and allassestResult:
        #     assestsExist.append(check)

print("Below are the names of Qualys installed on servers and on Qualys portal ")
print(f"{assestsExist}")
print(len(assestsExist))

# readName = re.findall(r"\w+-\w+", read[1])
# readName2Dash = re.findall(r"[\w-]+", read[1])
# dDash.append(readName2Dash)
# print(readMe)
