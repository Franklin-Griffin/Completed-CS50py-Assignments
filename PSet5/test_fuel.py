from fuel import convert, gauge
def test_convert():
	assert convert("49/100") == 49
def test_gauge():
	assert gauge(0) == "E"
	assert gauge(100) == "F"
	assert gauge(49) == "49%"
