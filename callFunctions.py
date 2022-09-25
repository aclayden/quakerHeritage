import csv
import getWebData as gwd

#collate all data
url = "https://heritage.quaker.org.uk/"
pdfList = gwd.getUrls(url)
dictList = []
#for pdf in pdfList ####DO NOT UNCOMMENT UNTIL GO LIVE####
for pdf in pdfList[1:2]:
    dictList.append(gwd.pdfDataExtract(pdf))  

#compile values into a csv
with open('D:\Documents\Coding\quakerHeritage\mycsvfile.csv','w', newline = '') as f:
    w = csv.writer(f)
    w.writerow(dictList[0].keys())
    for meetingHouse in dictList:
        w.writerow(meetingHouse.values())
    