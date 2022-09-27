import getWebData as gwd
import cleanseData as cd

url = "https://heritage.quaker.org.uk/"
filepath = 'D:\Documents\Coding\quakerHeritage\quakerHeritageDB.csv'

#query webpage for pdfs, collate data, and hygiene

def getOnlineData(url, filepath): 
    pdfList = gwd.getUrls(url)
    dictList = []
    for pdf in pdfList[1:51]: ####remove slice for full Go Live####
        dictList.append(gwd.pdfDataExtract(pdf))
    df = cd.createDataframe(dictList)
    df = cd.hygieneDataframe(df)
    cd.saveToCSV(df, filepath)

#load data from csv for testing purposes
df = cd.loadFromCSV(filepath)
print(df.head())  