tableData = [['apples', 'oranges', 'cherries', 'bananas'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']
			 ]

def printTable(table_data):

	#Get the length of each word and find the highest number
	list_length = []
	for row in table_data:
		for index, item in enumerate(row):
			list_length.append(len(item))

	list_length_order = sorted(list_length)
	max_len = list_length_order[-1]
	print(max_len)

	col_widths = [0] * len(table_data)
	# print(col_widths)
	
	# Display to table
	for r in zip(*table_data):
		data = ' '.join(r)
		print(data)

printTable(tableData)

# incomplete as unable to use the alignment within the 'for r' loop
