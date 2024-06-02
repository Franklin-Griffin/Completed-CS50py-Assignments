def main():
    while True:
        try:
            print("Fraction: ", end="")
            p = convert(input())
            print(gauge(p))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
def convert(fraction):
	x,y = fraction.split("/")
	if int(x) > int(y):
		raise ValueError
	return round((int(x) / int(y)) * 100)
def gauge(percentage):
	if percentage <= 1:
		return "E"
	elif percentage >= 99:
		return "F"
	else:
		return percentage + "%"
if __name__ == "__main__":
    main()
