import sys
if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")
elif sys.argv[1].split(".")[-1] != "csv":
	sys.exit("Not a CSV file")
elif sys.argv[2].split(".")[-1] != "csv":
	sys.exit("Not a CSV file")
else:
	try:
		with open(sys.argv[1], "r") as r:
			with open(sys.argv[2], "w") as w:
				x = r.readlines()
				w.write("first,last,house\n")
				for row in x[1:]:
					q = row.split(",")
					q[0] = q[0][1:]
					q[1] = q[1][:-1]
					w.write(q[1][1:]+","+q[0]+","+q[2])
	except:
		sys.exit("Could not read a file")
