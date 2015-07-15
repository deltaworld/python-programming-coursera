# Implementation of Person class
# http://www.codeskulptor.org/#exercises_classes_person_def_template.py


#################################################
# Student adds code where appropriate

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        
    def full_name(self):
    
    def age(self, current_year):
    
    def __str__(self):
 
    
###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

print joe
print john
print stephen
print scott

print joe.age(2013)
print scott.age(2013)   # yeah, right ;)
print john.full_name()
print stephen.full_name()


####################################################
# Output of testing code - results of __str__ method may vary

#The person's name is Joe Warren. Their birth year is 1961
#The person's name is John Greiner. Their birth year is 1966
#The person's name is Stephen Wong. Their birth year is 1960
#The person's name is Scott Rixner. Their birth year is 1987
#52
#26
#John Greiner
#Stephen Wong