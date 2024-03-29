import os
import datetime
import pyuac
import sys
from dateutil.relativedelta import relativedelta

def Setup():
    DirectoriesList = open("Directories.txt", "r")
    directories = DirectoriesList.readline().rstrip()
    DirectoriesList.close()

    FSFile = open("FileSizeMax.txt", "r")
    FileSizeMax = FSFile.readline().rstrip()
    FSFile.close()

    Exclusions = open("Exclusions.txt", "r")
    ExclusionList = [line.rstrip() for line in Exclusions]
    Exclusions.close()

    lastDate = datetime.datetime.now() - relativedelta(weeks=1)
    formattedDate = lastDate.strftime("%m/%d/%Y")
    print(directories, FileSizeMax, ExclusionList, formattedDate)
    return directories, FileSizeMax, ExclusionList, formattedDate


# Get clips in directory
def getFiles(dirs):
    dirlist = []
    dirlist = os.listdir(dirs)
    return dirlist


# Delete any clips older than the last date and larger than the MB set in the FileSizeMax.txt. Exclude any thing set in exclusions file.
def delFiles(files, FileSizeMax, ExclusionList, directories, lastdate):
    print(files)
    lDate = datetime.datetime.strptime(lastdate, "%m/%d/%Y")
    for file in files:
        print(file)
        path = os.path.join(directories, file)
        print(path)
        timecreated = os.path.getctime(path)
        size = os.path.getsize(path) >> 20
        date = datetime.datetime.fromtimestamp(timecreated).strftime("%m/%d/%Y")
        parseddate = datetime.datetime.strptime(date, "%m/%d/%Y")
        print(f'{file} created on {date} and is {size} MB\n')
        if date not in ExclusionList and size > FileSizeMax and parseddate <= lDate:
            print(f"Delete {file} {date} {size} MB")
            os.remove(path)


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        sys.exit()
    else:
        Setup()  # Already an admin here.
dirList, FileSizeMax, ExclusionList, lastmonth = Setup()
print(dirList)
print(FileSizeMax)
print(ExclusionList)
maxFile = int(FileSizeMax)
files = getFiles(dirList)
delFiles(files, maxFile, ExclusionList, dirList, lastmonth)