from bank import value
def test_hello():
	assert value("Hello") == "$0"
def test_hi():
	assert value("Hi") == "$20"
def test_greetings():
	assert value("Greetings") == "$100"
