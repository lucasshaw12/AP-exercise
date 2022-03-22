#! python3
# backupToZip - copies an entire folder and its contents into a ZIP files whos name increments
import zipfile, os


def backupToZip(folder):
	# backup the entire contents of 'folder' into a ZIP file

	folder = os.path.abspath(folder) # make sure folder is absolute

	# Figure out the filename this code should be used on what files already exist
	number = 1
	while True:
		zipFileName = os.path.basename(folder) + ' ' + str(number) + '.zip'
		if not os.path.exists(zipFileName):
			break
		number = number + 1

	# Create the ZIP file
	print(f'Creating {zipFileName}...')
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	# Walk the entire folder tree and compress the folders into a ZIP file
	for foldername, subfolders, filenames in os.walk(folder):
		print(f'Adding files in {foldername}...')
		# Add the current folder to the Zip file
		backupZip.write(foldername)

		# Add all files in this folder to the ZIP file
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue	#	don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()

	print('Done.')

backupToZip('/Users/Lucas/Python')