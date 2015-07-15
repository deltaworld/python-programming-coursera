# Implementation of Student class
# http://www.codeskulptor.org/#exercises_classes_student_def_template.py


#################################################
# Student adds code where appropriate

# definition of Student class
class Student:
    
    def __init__(self, name, pwd):
        
    def get_name(self):
    
    def check_password(self, pwd):
    
    def get_projects(self):
    
    def add_project(self, project):
        
 
    
###################################################
# Testing code

joe = Student("Joe Warren", "TopSecret")

print joe.get_name()
print joe.check_password("qwert")
print joe.check_password("TopSecret")

print joe.get_projects()
joe.add_project("Create practice exercises")
print joe.get_projects()
joe.add_project("Implement Minecraft")
print joe.get_projects()


####################################################
# Output of testing code 

#Joe Warren
#False
#True
#[]
#['Create practice exercises']
#['Create practice exercises', 'Implement Minecraft']


