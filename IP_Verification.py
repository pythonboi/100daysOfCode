import os
import re


ipList = "20.189.172.161", "40.126.29.11", "40.126.29.12", "52.168.116.128", "52.182.141.192", "159.203.55.55", \
         "184.168.130.131", "192.99.195.220", "204.79.197.200", "208.91.248.3", "208.91.248.3", "6.137.90.51"

newIpList = []

matchedIps = []

allIps = []

ip = "45.79.98.50"

with open(r"C:\Users\htukuru\OneDrive - Alithya\Desktop\ipchecklist.txt", 'r') as ipFile:
    ipread = ipFile.readlines()
    for read in ipread:
        newIpList.append(read.strip())

path = r"C:\Users\htukuru\Downloads\dns_entry"

for path, dirs, files in os.walk(path):
    print(files)
    print(len(files))
    for name in files:
        fullPath = os.path.join(path, name)
        # print(fullPath)
        with open(fullPath, 'r') as file:
            newFile = file.read()
            reFile = re.findall(r"\d+\.\d+\.\d+\.\d+", newFile)
            # print(reFile)
            for reads in reFile:
                if reads in newIpList:
                    print(f"IP found from {fullPath}", reads)
                    allIps.append(reads)

print(allIps)

uniqIPSet = set()

for uni in allIps:
    uniqIPSet.add(uni)

print(uniqIPSet)
