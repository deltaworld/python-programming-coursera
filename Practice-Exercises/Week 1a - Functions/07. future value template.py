# Compute the future value of a given present value, annual rate, and number of years.
# http://www.codeskulptor.org/#exercises_fn_future_value_template.py

###################################################
# Future value formula
# Student should enter function on the next lines.



###################################################
# Tests
# Student should not change this code.

def test(present_value, annual_rate, years):
	"""Tests the future_value function."""
	
	print "The future value of $" + str(present_value) + " in " + str(years),
	print "years at an annual rate of " + str(annual_rate) + "% is",
	print "$" + str(future_value(present_value, annual_rate, years)) + "."


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.1513572895656.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048000007.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.1112346694133.
