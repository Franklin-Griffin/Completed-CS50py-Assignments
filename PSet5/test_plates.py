from plates import is_valid
def test_cs50():
	assert is_valid("CS50")
def test_cs05():
	assert not is_valid("CS05")
def test_cs50p():
	assert not is_valid("CS50P")
def test_pi314():
	assert not is_valid("PI3.14")
def test_h():
	assert not is_valid("H")
def test_outatime():
	assert not is_valid("OUTATIME")