from random import random
n = 0
while not n in ["1", "2", "3"]:
	n = input("Level: ")
n = int(n)
correct = 0
questions = 0
while questions < 10:
	tries = 0
	a = int(random() * (10 ** n)) + 1
	b = int(random() * (10 ** n)) + 1
	ans = a + b
	resp = ""
	while True:
		if tries == 3:
			print(f"{a} + {b} = {ans}")
			break
		resp = input(f"{a} + {b} = ")
		if resp == str(ans):
			correct += 1
			break
		else:
			print("EEE")
			tries += 1
	questions += 1
print(f"Score: {correct}")
