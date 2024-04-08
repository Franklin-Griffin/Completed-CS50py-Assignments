def convert(x):
	return x.replace(":)", "🙂").replace(":(", "🙁")
def main():
	x = input()
	print(convert(x))
main()