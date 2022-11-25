import re
import csv

inventoryFound = []

allAssestsFound = []

assestsExist = []

qualysInstall = []

uniqueName = set()

internalAssets = r"C:\Users\htukuru\OneDrive - Alithya\Documents\myQualysData1.csv"

allAsessts = r"C:\Users\htukuru\Downloads\AI_Asset_List_athya9ht_20221122.csv"

with open(internalAssets, 'r') as file:
    myReader = csv.reader(file)
    for read in myReader:

        if read[2] == "Yes":
            qualysInstall.append(read[1].lower())

    for look in qualysInstall:
        # readMe = re.search(r"([\w+-]+)", read[1])
        readMe = re.search(r"([\w+-]+)", look)
        firstGroup = readMe.group()
        inventoryFound.append(firstGroup)
        # print(firstGroup)

    # print(qualysInstall)
    # print(len(qualysInstall))
    print(inventoryFound)
    print(len(inventoryFound))

    print("End of the Master Inventory data")
    print("##################################################################################")

    with open(allAsessts, "r") as asstFile:
        allAssestReader = csv.reader(asstFile)

        for newRead in allAssestReader:
            allassetsSearch = re.search(r"([\w+-]+)", newRead[2].lower())
            allassestResult = allassetsSearch.group()
            allAssestsFound.append(allassestResult)

            # print(allassestResult)

    for check in inventoryFound and allAssestsFound:
        if check in inventoryFound and allAssestsFound:
            assestsExist.append(check)
            # print(check)

    for unique in assestsExist:
        uniqueName.add(unique)

print("Below are the names of Qualys installed on servers and on Qualys portal ")
print(f"{assestsExist}")
print(len(assestsExist))

print(uniqueName)
print(len(uniqueName))
