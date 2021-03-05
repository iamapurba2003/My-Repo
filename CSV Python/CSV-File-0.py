import csv 

fileName = "C:/Users/Himangshu De/Desktop/CSV Python/CSV for Python - Sheet1.csv"



with open(fileName, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    for line in csvReader:
        if "Roll Number" in line:
            fields=list(line)
            print(f'The fields of the file is: {fields[:4]}')
        else:
            print(line)

            