print("Expression: ", end="")
x,y,z = input().split(" ")
if y == "+":
	print(int(x) + int(y))
elif y == "-":
	print(int(x) - int(y))
elif y == "*":
	print(int(x) * int(y))
else:
	print(int(x) / int(y))