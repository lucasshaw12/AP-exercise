#! python3
# removeCsvHeader - remove the headre from all csv files in current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True) # Ignores the folder if it already exists

# Loop through the files in the current working directory
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue # Skips non-csv files

	print('Removing header from ' + csvFilename + '... ')

	# Read the csv file
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # Skip the first row
		csvRows.append(row)
	csvFileObj.close()

	# Write out the csv file
	csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

	

