import csv, re

csvFile = r"C:\Users\htukuru\Downloads\LIst of computer with ESET versions.csv"

headers = []
rows = []
newHeaders = []

with open(csvFile, 'r') as myCSVFile:
    # print(myCSVFile)

    csvReader = csv.reader(myCSVFile, delimiter=";")

    headers = next(csvReader)

    for clean in headers:
        #print(clean)
        more = clean.strip("ï»¿")
        newHeaders.append(more)
        # noSign = re.findall(r'[a-zA-Z]+', clean)

    # noSign = re.search(r'\w+', headers)

    for row in csvReader:
        rows.append(row)



print(headers)
#print(noSign)
print(newHeaders)
print(rows)


# Writing to csv file

writeCSV = r'C:\Users\htukuru\Downloads\csvWrite.csv'

with open(writeCSV, 'w') as theFile:
    csvWriter = csv.writer(theFile)

    csvWriter.writerow(newHeaders)

    csvWriter.writerows(rows)