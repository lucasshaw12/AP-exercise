def runList(lists):
	if len(lists) == 1:
		return lists[0]
	return '{}, and {}'.format(', '.join(lists[:-1]), lists[-1])

spam = ['1', '2', '3', '4']
spamEmpty = []
spam1 = ['1', '2']

printlist = runList(spam)
print(printlist)

# # Source for the answer
# # https://stackoverflow.com/questions/38824634/automate-the-boring-stuff-with-python-comma-code
