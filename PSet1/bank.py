print("Greeting: ", end="")
x = input()
if "Hello" in x:
	print("$0")
elif x[0] == "H":
	print("$20")
else:
	print("$100")