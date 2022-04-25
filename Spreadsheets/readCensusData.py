#! python3

# Open and read the the cells using openpyxl
# Calculate all the tract and population data and store it in a data structure
# Write the data structure to a text file with .py extention using the pprint module

####################################################################
# This section needs to be ran once only, it creates the .py file and creates a dictionary from the data, 
# which is then used as a module in the section below
import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# Each row in the spreadsheet has data for one census tract
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value 
	pop = sheet['D' + str(row)].value

	# Make sure the key for this state exists
	countyData.setdefault(state, {})
	# Make sure the key for this county in this state exists
	countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

	# Each row represents one census tract, so increment by one
	countyData[state][county]['tracts'] += 1
	# Increase the county pop by the pop in this census tract
	countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')

####################################################################
import os, census2010 # imports the census2010.py as a module
print(census2010.allData['AK']['Anchorage'])
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))