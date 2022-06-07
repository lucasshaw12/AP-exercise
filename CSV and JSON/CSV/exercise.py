#! python3

import csv

#######################################################
# Reader objects

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][0])
# print(exampleData[0][1])
# print(exampleData[0][2])
# print(exampleData[1][1])
# print(exampleData[6][1])

#######################################################
# Reading reader objects using a for loop

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
# 	print(' Row #' + str(exampleReader.line_num) + ' ' + str(row))

#######################################################
# Writer objects

# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow((['spam', 'eggs', 'bacon', 'ham']))
# outputWriter.writerow(['Hello, world', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
# outputFile.close()

#######################################################
# Delimiter and lineterminator arguments

# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

#######################################################
# DictReader and DictWriter CSV objects

# exampleFile = open('exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)
# for row in exampleDictReader:
# 	print(row['Timestamp'], row['Fruit'], row['Quantity'])

#######################################################
# DictReader and DictWriter CSV objects without headers

# exampleFile = open('example.csv')
# exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
# for row in exampleDictReader:
# 	print(row['time'], row['name'], row['amount'])

# outputFile = open('output.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'] )
# outputDictWriter.writeheader()
# outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
# outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
# outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'Dog'})
# outputFile.close()
































