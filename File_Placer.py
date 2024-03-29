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
fullPath = ''

if currentDirectory != chgeDirectory:
    os.chdir(chgeDirectory)
    print(os.getcwd())

    qNewFolder = input("Do you want to create a new Folder: (Y/N) ").lower()
    if qNewFolder == 'y':

        newFolder = input("Please Enter the name of the new Folder: ").title()

        try:

            if newFolder not in chgeDirectory:
                os.mkdir(newFolder)
                print(f"{newFolder} folder created successful")

        except FileExistsError:
            print(f"{newFolder} folder already exists")

    else:

        if os.path.exists(chgeDirectory):

            lstDir = os.listdir(os.getcwd())
            for v in lstDir:
                getfileList += v

            print(len(lstDir), f"items in {chgeDirectory}")

        for check in lstDir:
            if os.path.isdir(check):
                folderSide.append(check)

            else:
                fileSide.append(check)

        for f in fileSide:

            if os.path.isfile(f):
                splitFileExt = os.path.splitext(f)

                fileName = splitFileExt[0]
                fileExt = splitFileExt[1]

                # Using regular Expression to separate the file extension from the file name

                for ext in fileExt:
                    regExt = re.search(r'\.(\w+)', fileExt)
                newfileExt.append(regExt.group(1))

        # Making the extension to be unique in the file

        for uni in newfileExt:
            newSet.add(uni.lower())

        print(newSet)
        print(len(newSet))

        # Creating the Folder from the file extension

        for uniqFile in newSet:
            try:
                if uniqFile in newSet:
                    os.mkdir(uniqFile)  # .title())
                    print(f"{uniqFile} created successfully")
            except FileExistsError:
                print(f"{uniqFile} already exists ")

        for vryFile in lstDir:

            if os.path.isfile(vryFile):
                fullPath = os.path.join(chgeDirectory, vryFile)

            for chkFolder in folderSide:

                getExistingDir = os.path.join(chgeDirectory, chkFolder)

                try:

                    for word in newSet:

                        if word in fullPath and word in getExistingDir:
                            print(shutil.move(fullPath.lower(), getExistingDir))

                        elif word not in fullPath and word in getExistingDir:
                            continue
                            # print(f"{word} already exit in {fullPath}")

                except shutil.Error:
                    print("file already exits")
                except FileNotFoundError:
                    print("No such file or directory")

# urlLink = "https://www.youtube.com/watch?v=n3IYVthup9I"
#
# urlLink2 = "https://www.youtube.com/watch?v=PAMpNhx4maM"

urlLink3 = "https://www.youtube.com/watch?v=isRtFdu8sRs"

urlLink4 = 'https://www.youtube.com/watch?v=yhIDVyxkmIk'

