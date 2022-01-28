import csv, sys
import os #library for checking if input file exists

def main(argv):
    if len(argv) != 3:
        print("error: parameters not sufficient")
        return
    exists = os.path.exists(argv[0])
    if exists:
        filename = argv[0]
    else:
        print("error: file name doesn't exist")
        return
    if argv[1] != "-d":
        print("error: " + argv[1] + " doesn't exist, try \"-d\"") 
        return
    if len(argv[2]) != 10:
        print("error: incorrect date format") 
        return
    date = argv[2]
    
    # opening the file
    file = open(filename)
    csvreader = csv.reader(file)
    if os.stat(filename).st_size == 0:
        print("error: csv file is empty")
        return
    header = next(csvreader)
    if len(header) != 2:
        print("error: number of file headers incorrect")
        return

    # dictionary has cookie names as keys and the number of occurences
    # of that cookie as values
    cookieDict = {}
    for row in csvreader:
        if row[1][:10] == date and row[0] in cookieDict.keys():
            cookieDict[row[0]] += 1
        elif row[1][:10] == date:
            cookieDict[row[0]] = 1
    file.close()

    #find max occurences and print cookies that have that value
    if len(cookieDict) == 0:
        print("error: no data in cvs file that matches input date")
        return
    dictVals = list(cookieDict.values())
    dictKeys = list(cookieDict.keys())
    maxDictVal = max(dictVals)
    for key in dictKeys:
        if cookieDict[key] == maxDictVal:
            print(key)

if __name__ == "__main__":
   main(sys.argv[1:])

# appropriate tests to run in command line 
# $python3 most_active_cookie.py
# $python3 most_active_cookie.py 123.csv
# $python3 most_active_cookie.py blank.csv -p
# $python3 most_active_cookie.py blank.csv -d 2020-1-5
# $python3 most_active_cookie.py blank.csv -d 2020-12-09
# $python3 most_active_cookie.py cookie_log.csv -d 2020-12-09
# $python3 most_active_cookie.py cookie_log.csv -d 2018-12-08
# $python3 most_active_cookie.py cookie_log.csv -d 2018-12-09