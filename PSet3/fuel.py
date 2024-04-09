while True:
	try:
		print("Fraction: ", end="")
		x,y = input().split("/")
		if int(x) > int(y):
			continue
		frac = int(x) / int(y)
		if frac <= 0.01:
			print("E")
		elif frac >= 0.99:
			print("F")
		else:
			print(f"{round(frac*100)}%")
	except (ValueError, ZeroDivisionError):
		continue
	else:
		break