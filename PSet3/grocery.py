items = {}
while True:
	try:
		item = input().upper()
		if item in items:
			items[item] += 1
		else:
			items[item] = 1
	except EOFError:
		items = dict(sorted(items.items()))
		for k,v in items.items():
			print(f"{v} {k}")
		break