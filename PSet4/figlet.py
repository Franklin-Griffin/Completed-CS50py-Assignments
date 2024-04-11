import sys
from pyfiglet import Figlet
f = Figlet()
if len(sys.args) > 1:
	if len(sys.args) != 3 or not sys.args[1] in ["-f", "--font"] or not sys.args[2] in f.getFonts():
		sys.exit("Invalid usage")
	f.setFont(sys.args[2])
	x = input()
	print(f.renderText(x))
else:
	x = input()
	print(f.renderText(x))