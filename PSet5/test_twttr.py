from twttr import shorten
def test_shorten():
	assert shorten("aeiou") == ""
	assert shorten("AEIOU") == ""
	assert shorten("twittery") == "twttry"
	assert shorten("123,./") == "123,./"