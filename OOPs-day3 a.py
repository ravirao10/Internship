# Parent classes
class Teacher:
    def teach(self):
        return "Teaching students"

class Researcher:
    def research(self):
        return "Conducting research"

# Child class 
class Professor(Teacher, Researcher):
    def guide(self):
        return "Guiding students in projects"

# Example usage
prof = Professor()
print(prof.teach())      # From Teacher
print(prof.research())   # From Researcher
print(prof.guide())      # From Professor
