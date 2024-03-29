# Compute a name tag, given the first and last name.
# http://www.codeskulptor.org/#exercises_fn_nametag_solution.py

###################################################
# Name tag formula
# Student should enter function on the next lines.
def name_tag(first_name, last_name):
	"""Returns a name tag string with the given name."""
	
    return "My name is " + first_name + " " + last_name + "."

	
###################################################
# Tests
# Student should not change this code.

def test(first_name, last_name):
	"""Tests the name_tag function."""
	
	print name_tag(first_name, last_name)
	
test("Joe", "Warren")
test("Scott", "Rixner")
test("John", "Greiner")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.
