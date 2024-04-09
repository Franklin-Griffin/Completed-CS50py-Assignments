items = {}
while True:
	try:
		print("Item: ", end="")
		item = input().lower()
		if item in items:
			items[item] += 1
		else:
			items[item] = 1
	except EOFError:
		items = dict(sorted(items.items()))
		for k,v in items:
			print(f"{v} {k}")
		break