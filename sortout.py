import re
import csv

inventoryFound = []

allAssestsFound = []

assestsExist = []

qualysInstall = []

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

        if read[2] == "Yes":
            qualysInstall.append(read[1].lower())

    print(qualysInstall)
    print(len(qualysInstall))

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
            pass

            # print(check)




print("Below are the names of Qualys installed on servers and on Qualys portal ")
print(f"{assestsExist}")
print(len(assestsExist))

