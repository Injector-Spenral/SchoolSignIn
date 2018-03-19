import csv
import datetime
import sys
from PIL import Image

def importCSV():
    #Import csv file into 'List' in and add the card to the dictionary for card scanning
    Info = []
    Dict = {'ListID' : 'CardID'}
    with open('IDMap.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            Info.append(row)
            Dict[row[0]] = i
            i += 1
    return Info, Dict
        
def scanCard(Info, Dict):
    card = input('Please scan card')
    fname = Info[Dict[card]][2]
    lname =	Info[Dict[card]][3]
    idnum = Info[Dict[card]][1]
    print("Hello, " + fname + " " + lname + ", " + idnum)
    return(card, idnum, fname, lname)


def logAttendance(card, id, room):
    with open('Log.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar = '|')
        spamwriter.writerow([datetime.datetime.isoformat(datetime.datetime.now()), card, id, room])

def showImage(id):
	image = Image.open(str(id) + ".jpg")
	image.show()
	
Info, Dict = importCSV()
card, idnum, fname, lname = scanCard(Info, Dict)
logAttendance(card, idnum, sys.argv[1])
showImage(idnum)
