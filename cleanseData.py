import pandas as pd
import getWebData as gwd

# collate all data
def createDataframe(url):
    pdfList = gwd.getUrls(url)
    dictList = []
    data = []
    for pdf in pdfList[1:4]:
        dictList.append(gwd.pdfDataExtract(pdf))  
    data.append([i for i in dictList[0].keys()])
    for dct in dictList:
        data.append([i for i in dct.values()])
    df = pd.DataFrame(data, columns = data[0])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    return df

#transform differing data to create consistentcy in the database 
def hygieneDataframe(df):
    df['Date'] = df['Date'].str.extract(r'^(\d{4})', expand=False)
    
    return df


#convert string dates to workable dates
# testDate = df.at[0, "Date of visit"]
# testDate = pd.to_datetime(testDate, errors='raise',dayfirst=True)
# testDate += pd.offsets.DateOffset(years=5)
# print(testDate)

df = createDataframe("https://heritage.quaker.org.uk/")
df = hygieneDataframe(df)
print(df['Date'])