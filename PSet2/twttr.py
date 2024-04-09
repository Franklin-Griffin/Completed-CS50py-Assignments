print("Input: ", end="")
x = input()
out = ""
for i in x:
	if not i in "aeiou":
		out += i
print(f"Output: {out}")