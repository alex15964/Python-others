import csv

outputdict2 = [('1','2','3'),('4','5','6'),('7','8','9')]

with open('test.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(outputdict2)