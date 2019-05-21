def readFile(filename):
	try:
		f = open(filename, "r")
	except IOError:
		print("File not found")
		exit(2)
	if f.mode != "r":
		exit(0)
	lines = f.readlines()
	f.close()
	return lines