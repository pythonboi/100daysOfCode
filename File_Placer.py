import shutil, re, os
# from CreateFolder import Folder
from pytube import YouTube

currentDirectory = os.getcwd()
print(currentDirectory)

chgeDirectory = input("Please Copy the directory you want to change to: ")

folderSide = []
fileSide = []
getfileList = ' '
newfileExt = []
newSet = set()

print(type(newSet))

if currentDirectory != chgeDirectory:
    os.chdir(chgeDirectory)
    print(os.getcwd())

    qNewFolder = input("Do you want to create a new Folder: (Y/N) ").lower()
    if qNewFolder == 'y':

        newFolder = input("Please Enter the name of the new Folder: ").title()

        if os.path.exists(chgeDirectory):
            # for v in chgeDirectory:
            #     print(v)

            lstDir = os.listdir(os.getcwd())
            for v in lstDir:
                getfileList += v

            # print(getfileList)
            # print(os.path.join(chgeDirectory, getfileList))
            # print(lstDir)
            print(len(lstDir), f"items in {chgeDirectory}")

        for check in lstDir:
            if os.path.isdir(check):
                folderSide.append(check)

            else:
                fileSide.append(check)

        print("Here is folder/directory section below: ")
        print("=======================================================================================================")

        print(folderSide)
        print(len(fileSide))
        fullPath = ''
        # for v in folderSide:
        #     fullPath += os.path.join(chgeDirectory, v)

        if newFolder not in folderSide:
            os.mkdir(newFolder)

            print(f"{newFolder} folder created successful")
        else:
            print(f"{newFolder} folder already exits")
            # exit()

        if os.path.exists(fullPath):
            print("Yes")

        # Differentiate the file from the extension

        for f in fileSide:

            if os.path.isfile(f):
                splitFileExt = os.path.splitext(f)

                fileName = splitFileExt[0]
                fileExt = splitFileExt[1]

                # print(fileExt)
                # print(splitFileExt)

                # Using regular Expression to separate the file extension from the file name

                for ext in fileExt:
                    regExt = re.search(r'\.(\w+)', fileExt)
                newfileExt.append(regExt.group(1))

        # print(newfileExt)

        # Making the extension to be unique in the file

        for uni in newfileExt:
            newSet.add(uni.lower())

        print(newSet)

        print("Here is the second set side")
        print(len(newSet))

# Creating the Folder from the file extension

        for uniqFile in newSet:
            try:
                if uniqFile in newSet:
                    os.mkdir(uniqFile.title())
                    print(f"{uniqFile} created successfully")
            except FileExistsError:
                print(f"{uniqFile} already exists ")


            # else:
            #     print(f"{uniqFile} already exists ")

        #
        #         else:
        #             print(f"{exf} already exits")
        # except:
        #
        #     print(f"{newfileExt}. created successful")

        # print(splitFileExt)

        # print(fullPath)

        # newFolder = input("Please Enter the name of the new Folder: ").title()
        # if os.path.exists(newFolder):
        #
#
# urlLink = "https://www.youtube.com/watch?v=n3IYVthup9I"
#
# urlLink2 = "https://www.youtube.com/watch?v=PAMpNhx4maM"
#
#
# mvFolder = shutil.move(chgeDirectory, )
