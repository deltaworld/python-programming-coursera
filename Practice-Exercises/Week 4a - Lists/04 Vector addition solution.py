# Vector addition function
# http://www.codeskulptor.org/#exercises_lists_add_solution.py

###################################################
# Student should enter code below

def add_vector(v, w):
    sum = [v[0] + w[0], v[1] + w[1]]
    return sum


###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]


###################################################
# Note that the plus operator concatenates  ("joins") 
# the two lists together

print [1, 2] + [3, 4]