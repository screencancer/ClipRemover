import os
import datetime


def Setup():
    Directories = open("Directories.txt", "r")
    dir = Directories.readline().rstrip()
    Directories.close()

    FSFile = open("FileSizeMax.txt", "r")
    FileSizeMax = FSFile.readline().rstrip()
    FSFile.close()

    Exclusions = open("Exclusions.txt", "r")
    ExclusionList = [line.rstrip() for line in Exclusions]
    Exclusions.close()

    return dir, FileSizeMax, ExclusionList


#Get clips in directory
def getFiles(dirs):
    list = []
    list= os.listdir(dirs)
    return list


# Delete any clips older than 15 days old and larger than 200 MB. Exclude any thing set in exclusions file.
def delFiles(files, FileSizeMax, ExclusionList, dirs):
    print(files)
    for file in files:
        print(file)
        path = os.path.join(dirs, file)
        print(path)
        timecreated = os.path.getctime(path)
        size = os.path.getsize(path) >> 20
        date = datetime.datetime.fromtimestamp(timecreated).strftime("%m/%d/%Y")
        print(f'{file} created on {date} and is {size} MB\n')
        if date not in ExclusionList and size > FileSizeMax:
            print(f"Delete {file} {date} {size} MB")



dirList, FileSizeMax, ExclusionList = Setup()
print(dir)
print(FileSizeMax)
print(ExclusionList)

maxFile = int(FileSizeMax)
files = getFiles(dirList)
delFiles(files, maxFile, ExclusionList, dirList)