# String list joining problem
# http://www.codeskulptor.org/#exercises_mouse_join_solution.py

###################################################
# Student should enter code below

def string_list_join(string_list):
    ans = ""
    for i in range(len(string_list)):
        ans += string_list[i]
    return ans


###################################################
# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


###################################################
# Output

#
#catdog
#spam and eggs
#abcd