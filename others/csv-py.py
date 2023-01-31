import csv

file=open('TitanicSurvival.csv','r')
data=list(csv.reader(file,delimiter = "."))
file.close()

print(data)
