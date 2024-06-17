import sys
from tabulate import tabulate
if len(sys.argv) < 2:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
elif sys.argv[1].split(".")[-1] != "csv":
	sys.exit("Not a CSV file")
else:
	try:
		with open(sys.argv[1], "r") as f:
			x = f.readlines()
			header = x[0]
			body = []
			for row in x[1:]:
				body.append(row.split(","))
			print(tabulate(body, header, tablefmt="grid"))
	except:
		sys.exit("File does not exist")
