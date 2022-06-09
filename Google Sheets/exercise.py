#! python3
# 

import ezsheets

#################################################
# Viewing a spreadsheet

# ss = ezsheets.Spreadsheet('1WBsyALO7oKFvx-GJZjfiIFspb-BUUjmAooxbPEW0qQ0')
# print(ss)
# print(ss.title)

#################################################
# Creating a spreadsheet

# ss = ezsheets.createSpreadsheet('Title of my new spreadsheet')
# print(ss)
# print(ss.title)

#################################################
# Upload an existing spreadsheet

# ss = ezsheets.upload('my_spreadsheet.xlsx')
# print(ss.title)

#################################################
# List Google Drive spreadsheets

# ss = ezsheets.listSpreadsheets()
# print(ss)

#################################################
# Accessing and manipulating spreadsheets

# ss = ezsheets.Spreadsheet('144DzfJIkpCo57lSymTrhopGfToFv4ImCQBopVxysg38')
# print(ss.title)
# ss.title = 'Class Data' # Change the title
# print(ss.title)
# print(ss.spreadsheetId) # This is read-only as its and ID
# print(ss.url) # This is read-only as its and ID
# print(ss.sheetTitles) # The titles of all the Sheet objects
# print(ss.sheets) # The sheet objects in order
# print(ss[0]) # Access the first sheet object in the workbook
# print(ss['Sheet1']) # Access the sheet by title. This will cause an error if the sheet name does not exist
# del ss[0] # Delete the first spreadsheet
# print(ss.sheetTitles)
# ss.refresh() # Use this if the sheet is amended via the Google Sheets website

#################################################
# Downloading and uploading spreadsheets

# ss = ezsheets.Spreadsheet('144DzfJIkpCo57lSymTrhopGfToFv4ImCQBopVxysg38')
# print(ss.title)
# ss.downloadAsExcel() # Downloads as an excel file
# ss.downloadAsODS() # Downloads as an openoffice file
# ss.downloadAsCSV() # Only downloads the first sheet as a CSV file
# ss.downloadAsTSV() # Only downloads the first sheet as TSV file
# ss.downloadAsPDF() # Only downloads the first sheet as a PDF
# ss.downloadAsHTML() # Only downloads the first sheet as a ZIP of a HTML file

#################################################
# Deleting spreadsheets

# ss = ezsheets.createSpreadsheet('Delete me')
# print(ezsheets.listSpreadsheets())
# ss.delete('Delete me') # Sent the spreadsheet to trash
# ss.delete('Delete me', permanent=True) # Permamnantly delete the spreadsheet
# ss.refresh()
# print(ezsheets.listSpreadsheets())

#################################################
# Spreadsheet sheet objects

# ss = ezsheets.Spreadsheet('1TfuBE3q-wEExdc1oZG-rWKWyPffB1DWz7U7Njf-eSkc')
# print(ss.sheets) # The sheet objects of this ss in order
# print(ss.sheets[1]) # Gets the first sheet object
# print(ss[1]) # Same as the above, also gets the first sheet object
# print(ss.sheetTitles) # Titles of all the sheets in this spreadsheet
# print(ss['Sheet4']) # Access sheet by title

#################################################
# Reading and writing data

# ss = ezsheets.createSpreadsheet('My spreadsheet')
# sheet = ss[0] # Get the first sheet
# print(sheet.title)
# sheet['A1'] = 'Name'
# sheet['B1'] = 'Age'
# sheet['C1'] = 'Favourite Movie'
# print(sheet['A1'])
# print(sheet['A2']) # Empty cells run a blank string
# print(sheet[2, 1]) # column 2, row 1 is the same as 'B1'
# sheet['A2'] = 'Lucas'
# sheet['B2'] = '29'
# sheet['C2'] = 'Beverly Hills Cop'

#################################################
# Column and Row addressing

# ezsheets.convertAddress('A2') # converts address
# ezsheets.convertAddress(1, 2) # converts address back
# print(ezsheets.getColumnLetterOf(2))
# print(ezsheets.getColumnNumberOf('B'))
# print(ezsheets.getColumnLetterOf(999))
# print(ezsheets.getColumnNumberOf('ZZZ'))


#################################################
# Upload, then reading and writing entire columns or rows

# ss = ezsheets.upload('produceSales.xlsx') # To upload a spreadsheet
# ss = ezsheets.Spreadsheet('produceSales')
# sheet = ss[0]
# print(sheet.getRow(1)) # the first row is 1, not 0
# print(sheet.getRow(2))
# columnOne = sheet.getColumn(1)
# print(sheet.getColumn(1))
# print(sheet.getColumn('A')) # Same result as getColumn(1)
# print(sheet.getRow(3))
# sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230']) # Set these values to row 3
# print(sheet.getRow(3)) # Check the above update has worked

# columnOne = sheet.getColumn(1)
# for i, value in enumerate(columnOne):
# 	columnOne[i] = value.upper() # Make the python list contain uppercase strings
# sheet.updateColumn(1, columnOne) # update the entire column in one request

# sheet = ss[0]
# rows = sheet.getRows() # Get every row in the spreadsheet
# print(rows[0]) # Examine the values of the first row
# print(rows[1])
# rows[1][0] # Change the produce name
# print(rows[1])
# print(rows[10])
# rows[10][2] = '400' # Change the pounds sold
# rows[10][3] = '904' # Change the total
# print(rows[10])
# sheet.updateRows(rows) # Update the online spreadsheet with the changes

# sheet = ss[0]
# print(sheet.rowCount)
# print(sheet.columnCount)
# sheet.columnCount = 4 # Change the columns to 4
# print(sheet.columnCount)

#################################################
# Creating and deleting sheets

# ss = ezsheets.createSpreadsheet('Multiple Sheets')
# print(ss.sheetTitles)
# ss.createSheet('Spam') # Create a new sheet called Spam
# ss.createSheet('Eggs') # Create another sheet called Eggs
# print(ss.sheetTitles)
# ss.createSheet('Bacon', 0) # Create a sheet at index 0
# print(ss.sheetTitles)

# ss[0].delete()
# print(ss.sheetTitles)
# ss['Spam'].delete()
# print(ss.sheetTitles)
# sheet = ss['Eggs'] # Assign a variable to the Eggs sheet
# sheet.delete() # Delete the eggs sheet
# print(ss.sheetTitles)
# ss[0].clear()
# print(ss.sheetTitles)

#################################################
# Copying sheets

# ss1 = ezsheets.createSpreadsheet('First spreadsheet')
# ss2 = ezsheets.createSpreadsheet('Second spreadsheet')
# print(ss1[0])
# ss1[0].updateRow(1, ['some', 'data', 'in', 'the', 'first', 'row'])
# ss1[0].copyTo(ss2) # Copy ss1 Sheet1 to the ss2 spreadsheet
# print(ss2.sheetTitles)



















