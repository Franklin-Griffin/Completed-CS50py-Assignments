import sys
import requests
n = 0
try:
	n = float(sys.args[1])
except Exception:
	sys.exit("Invalid arg")
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json
cost = r["bpi"]["USD"]["rate_float"] * n
print(f"${cost:,.4f}")