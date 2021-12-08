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


TextFile = "C:\\Users\htukuru\\Downloads\\New folder (3)\\"

os.chdir(TextFile)

myDir = os.listdir(TextFile)

print(myDir)

with open(myDir[3]) as file:
    km = file.read()
    # info = re.findall(r"(\d+)\s+\d+\s.+\s+\d\s\w+\s+\w+\s+\d+\s", km)
    info1 = re.findall(r"(\d+\s\w+\s+\d+\s+\d+\s+.+)", km)
    info2 = re.findall(r"\d+\s\w+\s+\d+\s+[0-9][0-9]\:[0-9][0-9].+", km)
    # print(info)

    # size, data = info[0], info[1]

    # print(file.read())

with open("FileData", 'w') as oneFile:
    for a in info1:
        listString = str(a)
        print(listString)
        # oneFile.writelines(listString)



# print(size + data)
# print(info1)
#print(info2)
