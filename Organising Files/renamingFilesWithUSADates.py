#! python3
# Rename files with USA dates format to European date formats
# CHECK THAT LINE 40 IS COMMENTED FOR TESTING PURPOSES AS THIS CANNOT BE UNDONE

import shutil, os, re

# Create a regex that macthes files with an American date format
datePattern = re.compile(r"""^(.*?) # all text before the date
	((0|1)?\d)-			# Match a month
	((0|1|2|3)?\d)-		# Match a day
	((19|20)\d\d)		# Match a year
	(.*?)$				# all text after the date 
	""", re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# skip files with a date
	if mo == None:
		continue # skips the rest of the loop and moves onto the next filename within the loop

	# Get the different parts of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the european style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# get the full absolue filepaths
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# rename the files
	print(f'Renaming "{amerFilename}" to "{euroFilename}"... ')
	#shutil.move(amerFilename, euroFilename) # UNCOMMENT AFTER TESTING 

