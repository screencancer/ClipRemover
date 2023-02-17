import os
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parser


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

    lastDate = datetime.datetime.now() - relativedelta(weeks=1)
    formattedDate = lastDate.strftime("%m/%d/%Y")
    return dir, FileSizeMax, ExclusionList, formattedDate


#Get clips in directory
def getFiles(dirs):
    list = []
    list= os.listdir(dirs)
    return list


# Delete any clips older than the last date and larger than the MB set in the FileSizeMax.txt. Exclude any thing set in exclusions file.
def delFiles(files, FileSizeMax, ExclusionList, dirs, lastdate):
    print(files)
    lDate = datetime.datetime.strptime(lastdate,"%m/%d/%Y")
    for file in files:
        print(file)
        path = os.path.join(dirs, file)
        print(path)
        timecreated = os.path.getctime(path)
        size = os.path.getsize(path) >> 20
        date = datetime.datetime.fromtimestamp(timecreated).strftime("%m/%d/%Y")
        parseddate = datetime.datetime.strptime(date, "%m/%d/%Y")
        print(f'{file} created on {date} and is {size} MB\n')
        if date not in ExclusionList and size > FileSizeMax and parseddate <= lDate:
            print(f"Delete {file} {date} {size} MB")
            os.remove(path)


dirList, FileSizeMax, ExclusionList, lastmonth = Setup()
print(dir)
print(FileSizeMax)
print(ExclusionList)
maxFile = int(FileSizeMax)
files = getFiles(dirList)
delFiles(files, maxFile, ExclusionList, dirList, lastmonth)