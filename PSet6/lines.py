import sys
if len(sys.argv) < 2:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
elif sys.argv[1].split(".")[-1] != "py":
	sys.exit("Not a python file")
else:
	try:
		with open(sys.argv[1], "r") as f:
			count = 0
			for line in f.readlines():
				if not (line.strip() == "" or line.strip().startswith("#")):
					count += 1
			sys.exit(str(count))
	except:
		sys.exit("File does not exist")
