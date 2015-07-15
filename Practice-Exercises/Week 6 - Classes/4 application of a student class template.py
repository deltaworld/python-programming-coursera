# Use of the Student class
# http://www.codeskulptor.org/#exercises_classes_student_use_template.py


# definition of Student class
class Student:
    
    def __init__(self, name, pwd):
        self.full_name = name
        self.password = pwd
        self.projects = []
        
    def get_name(self):
        return self.full_name
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)


#################################################
# Student adds code where appropriate
        
# definition of function assign
def assign(students, name, pwd, project):    
        
 
    
###################################################
# Testing code

# create some Student objects
joe = Student("Joe Warren", "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student("Scott Rixner", "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student("John Greiner", "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()



####################################################
# Output of testing code 

#['Create practice exercises', 'Implement Minecraft']
#['Create practice exercises', 'Implement Minecraft', 'Practice RiceRocks']
#[]
#[]
#['Work on reflexes']

