import inflect
people = []
while True:
	try:
		person = input("Name: ")
		people.append(person)
	except EOFError:
		break
p = inflect.engine()
print(f"Adieu, adieu, to {p.join(people)}")