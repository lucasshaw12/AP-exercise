#! python3
# myclip.py - a Multi Clipboard Program

TEXT = {'agree': '''Yes, I agree, that sounds fine to me''',
		'busy': '''Sorry, can we do this next week or later this week''',
		'upsell': '''Would you consider making this a monthly donation''' }

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: py mclip.py [keyphrase] - copy phrase text')
	sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
	pyperclip.copy(TEXT[keyphrase])
	print('Text for ' + keyphrase + ' copied to the clipboard')
else:
	print('There is no text for ' + keyphrase)

# Usage
# Run this python script in terminal or run 'mclip.command' from spotlight
# Then run this file again + a keyphrase e.g 'python mclip.py agree'