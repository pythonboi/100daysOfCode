import re


myFile = []

with open("DateFile") as file:
    sht = file.read()
    mk = re.findall(r".\.\d\w(\s\w+\s+\d+\s+\d{4}\s.+)", sht)
    mk2 = re.findall(r".\.\d\w(\s\w+\s+\d+\s+[0-9][0-9]\:[0-9][0-9]+\s\w+.+)", sht)

    print(mk)
    print(mk2)

# print(myFile)

with open("updateData", 'w') as newFile:
    for m in mk:
        oFile = str(m)
        print(oFile)
        newFile.writelines(oFile + "\n")
    for n in mk2:
        nFile = str(n)
        newFile.writelines(nFile + "\n")

