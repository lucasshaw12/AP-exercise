#! python3
# multiClipboard.pyw # Saves and loads pieces of text to a clipboard
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
# Usage: mcb.pyw <keyword> - Loads keyword to clipboard
# Usage: mcb.pyw list - loads all keywords to a list
# mcb = multiClipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()