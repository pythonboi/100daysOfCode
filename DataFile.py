import re
import os

#
#
# myFile = []
#
# with open("DateFile") as file:
#     sht = file.read()
#     mk = re.findall(r".\.\d\w(\s\w+\s+\d+\s+\d{4}\s.+)", sht)
#     mk2 = re.findall(r".\.\d\w(\s\w+\s+\d+\s+[0-9][0-9]\:[0-9][0-9]+\s\w+.+)", sht)
#
#     print(mk)
#     print(mk2)
#
# # print(myFile)
#
# with open("updateData", 'w') as newFile:
#     for m in mk:
#         oFile = str(m)
#         print(oFile)
#         newFile.writelines(oFile + "\n")
#     for n in mk2:
#         nFile = str(n)
#         newFile.writelines(nFile + "\n")
#


# TextFile = "C:\\Users\htukuru\\Downloads\\New folder (3)\\"
#
# os.chdir(TextFile)
#
# myDir = os.listdir(TextFile)
#
# print(myDir)
#
# myDir.remove("FileData.txt")
#
# myFile = open("TheFile", 'w')
#
# print(myDir)

# getList = []

# with open("TheFile") as file:
# with open(myDir[4], 'r') as file:
#     myFile.write(file.read())
    # km = file.read()
    # with open("TheFile", 'w') as newFile:
    #     for g in file:
    #         print(g)
    #         newFile.write(g)
    # myFile = file.writelines(km)
    # info = re.findall(r"(\d+)\s+\d+\s.+\s+\d\s\w+\s+\w+\s+\d+\s", km)
    # info1 = re.findall(r"(\d+\s\w+\s+\d+\s+\d+\s+.+)", km)
    # info2 = re.findall(r"\d+\s\w+\s+\d+\s+[0-9][0-9]\:[0-9][0-9].+", km)

# with open("FileData", "w") as oneFile:
#     for m in info1:
#         # lFile = getList.append(m)
#         mFile = str(m)
#         oneFile.writelines(mFile + "\n")

# print(getList)

# print(myFile)
#
# myFile.close()

with open("modifiedDatePlus") as goFile:
    mi = goFile.read()
    yourFile = open("TheFile", 'w')
    first = re.findall(r"(\d+\s\w+\s+\d+\s+\d+\s+.+)", mi)
    second = re.findall(r"\d+\s\w+\s+\d+\s+[0-9][0-9]\:[0-9][0-9].+", mi)
    for v in first:
        yourFile.writelines(v + "\n")
    for m in second:
        yourFile.writelines(m + "\n")
    # yourFile.write(mi)
    yourFile.close()
