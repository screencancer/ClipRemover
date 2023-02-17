import datetime as dt
import os

# Set new exclusion date
def setExclusionDate():
    date = input("Input a date in the Format MM/DD/YYYY\n")
    dt.datetime.strptime(date, "%m/%d/%Y")
    file = open('Exclusions.txt', 'a+')
    file.write(date + "\n")
    file.close()
    print(f'Successfully added {date} to your Excluded Dates')
    Menu()

# Set file size max.
def setFileMax():
    while True:
        try:
            maxFileSize = int(input("Enter how many MB should be maximum on a file?\n"))
            break
        except:
            print("Invalid option you need an integer. Example: 500")
    file = open('FileSizeMax.txt', 'w')
    file.write(str(maxFileSize))
    file.close()
    print(f'Successfully added {maxFileSize} to your MaxFileSize')
    Menu()


# Set file directories to work in.
def setDir():
    while True:
        try:
            path = input("Give a directory path\n")
            if os.path.exists(path):
                break
            else:
                raise Exception("Not a valid path")
        except:
            print("Invalid option you need to give a path")
    file = open('Directories.txt', 'a+')
    file.write(path + "\n")
    file.close()
    print(f'Successfully added {path} to Directories')
    Menu()


# Menu
def Menu():
    option = input("1. Set a new Exclusion date \n"
                   "2. Set max file size to keep\n"
                   "3. Set file directory for the deletion\n")
    if (int(option)) == 1:
        setExclusionDate()
    elif (int(option)) == 2:
        setFileMax()
    elif (int(option)) == 3:
        setDir()


Menu()
