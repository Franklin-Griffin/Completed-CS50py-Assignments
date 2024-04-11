from random import random
level = -1
while level < 0:
	try:
		level = int(input("Level: "))
	except Exception:
		continue
myNum = int(random() * level + 1)
while True:
	try:
		guess = int(input("Guess: "))
		if guess == myNum:
			print("Just right!")
			break
		if guess > myNum:
			print("Too large!")
		if guess < myNum:
			print("Too small!")
	except Exception:
		continue