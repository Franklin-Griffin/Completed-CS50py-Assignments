import random


def main():
	correct = 0
	questions = 0
	level = get_level()
	while questions < 10:
		tries = 0
		a = generate_integer(level)
		b = generate_integer(level)
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


def get_level():
	n = 0
	while not n in ["1", "2", "3"]:
		n = input("Level: ")
	return int(n)


def generate_integer(level):
	return random.randint(10**(level-1) - (1 if level == 0 else 0), 10**level-1)


if __name__ == "__main__":
	main()