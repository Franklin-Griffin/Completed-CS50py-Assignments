import sys
from pyfiglet import Figlet
f = Figlet()
if len(sys.argv) > 1:
	if len(sys.argv) != 3 or not sys.argv[1] in ["-f", "--font"] or not sys.argv[2] in f.getFonts():
		sys.exit("Invalid usage")
	f.setFont(font=sys.argv[2])
	x = input()
	print(f.renderText(x))
else:
	x = input()
	print(f.renderText(x))