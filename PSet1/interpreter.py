print("Expression: ", end="")
x,y,z = input().split(" ")
if y == "+":
	print(float(int(x) + int(z)))
elif y == "-":
	print(float(int(x) - int(z)))
elif y == "*":
	print(float(int(x) * int(z)))
else:
	print(float(int(x) / int(z)))