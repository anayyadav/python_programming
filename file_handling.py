#open a file
# r - open a file for reading
# w - open a file for writing 
# x - open a file for exclusive creation. If the file already exits, the operation fails.
# a - open for appending at the end 
# t - open in text mode
# b - open in binary mode
# + - open a file for updating(reading and writing)
try:
	fw= open("test.txt", mode = 'w',encoding = 'utf-8' )
	# perform file operation 
	fw.write("my first file\n")
finally:
	fw.close()
	
try:
	fr = open("test.txt",mode='r',encoding='utf-8')
	fr.read(4) # reading first 4 data
	fr.read()
finally:
	fr.close()