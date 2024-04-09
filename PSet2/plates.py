def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
	if len(s) < 2 or len(s) > 6:
		return False
	startNums = False
	for i in range(len(s)):
		if not s[i].isalpha() and not s[i].isnumeric():
			return False
		if i <= 1 and not s[i].isalpha():
			return False
		if s[i].isalpha() and startNums:
			return False
		if s[i] == "0" and not startNums:
			return False
		if s[i].isnumeric():
			startNums = True
	return True
main()