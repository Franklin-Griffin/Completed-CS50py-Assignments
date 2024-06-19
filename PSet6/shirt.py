import sys
from PIL import Image, ImageOps
if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")
elif not sys.argv[1].split(".")[-1] in ["jpg","jpeg","png"]:
	sys.exit("Not an image file")
elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
	sys.exit("Extensions do not match")
else:
	try:
		with Image.open(sys.argv[1]) as img:
			shirt = Image.open("shirt.png")
			img = ImageOps.fit(img, shirt.size)
			img.paste(shirt, shirt)
			img.save(sys.argv[2])
	except:
		sys.exit("Could not read a file")
