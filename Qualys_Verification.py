import re
import csv

qAssets = r"C:\Users\htukuru\OneDrive - Alithya\Documents\myQualysData1.csv"

allAssets = r"C:\Users\htukuru\Downloads\AV_assets_athya9ht_20221119.csv"

fullAssets = r"C:\Users\htukuru\Downloads\AI_Asset_List_athya9ht_20221122.csv"

newEntry = []

allEntry = []

nameExists = []

prefix = []

newNameExits = []

withYes = []

newPrefixWithDot = []

yesNotShow = []

toronto = []

getAlithyaRegrx = []

with open(qAssets, 'r') as dFile:
    csvRead = csv.reader(dFile)
    csvReader = csv.DictReader(dFile)
    # print(csvRead)
    for check in csvRead:

        # invRegrex = re.findall(r"[\w-]+", check)
        # newRegrex = invRegrex[0]
        # getAlithyaRegrx.append(newRegrex)

        newEntry.append(check[1].lower())

        if check[2] == 'Yes':
            withYes.append(check[1].lower())

        if check[0] == "Toronto" and check[2] == "Yes":
            toronto.append(check[1].lower())

        # print(check)

    for check[1] in withYes:
            #print(h)
        invRegrex = re.findall(r"[\w-]+", check[1])
        newRegrex = invRegrex
        getAlithyaRegrx.append(newRegrex)

print(f"This is from Alithya Regrex master inventory {getAlithyaRegrx}")

print(f"This is the Total of all Inventory from the Master Inventory list {len(newEntry)}")
# print(f"This is from newEntry from master inventory list: {newEntry} ")
# print(withYes)
print(f"Here is the total number of Qualys Install with Yes {len(withYes)}")
# print(len(withYes))



with open(fullAssets, 'r') as file:
    Reader = csv.reader(file)

    for read in Reader:
        allEntry.append(read[2].lower())

        for call in allEntry:
            #     dsearch = re.search(r"[\w-]+", call)
            #
            # print(dsearch.group())

            prefixName = re.findall(r"[\w+\.\w-]+", call)
            prefixDot = re.findall(r"[\w-]+", call)

            newPrefix = prefixName[0]
            newPrefixDot = prefixDot[0]

        # print(prefixName[0])

        prefix.append(newPrefix)
        newPrefixWithDot.append(newPrefixDot)

        # for newCall in allEntry:

    for qs in withYes:
        if qs in prefix:
            newNameExits.append(qs)
        elif qs in newPrefixWithDot:
            newNameExits.append(qs)
        # elif qs not in newNameExits and check[0] == "Toronto":
        #     toronto.append(qs)
        elif qs not in newNameExits:
            yesNotShow.append(qs)
    print("#########################################################################")
    print("This is section printing with the Regrex Use for all assests!!!")
    # print(prefix)
    print(len(prefix))

    print("Here is with the dot for just the prefix name only ")
    # print(newPrefixWithDot)
    print(len(newPrefixWithDot))

# for m in newEntry:
#     if m in allEntry:
#         nameExists.append(m)
#
# for n in newEntry:
#     if n in prefix:
#         newNameExits.append(n)

# this print the name without the regrex
# print(nameExists)
# print(len(nameExists))

#
# print(allEntry)
# print(len(allEntry))

# This print the name with the regrex

print("This is with the Regrex below:")
print(newNameExits)
print(len(newNameExits))

# To get Qualys with Yes and not found on the Qualys Web portal

# print(f"Qualys with Yes but not showing as name exists {yesNotShow}")
# print(f"Number of Yes installed but not showing in Qualys {len(yesNotShow)}")


# to Get Toronto servers

# print(f"This is for Toronto Site: {toronto}")
# print(f"this is the total count of Toronto server {len(toronto)}")

#
# for h in newEntry:
#
    # invRegrex = re.findall(r"[\w-]+", h)
    # getAlithyaRegrx.append(invRegrex)


