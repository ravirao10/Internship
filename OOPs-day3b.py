# Base class
class Grandparent:
    def legacy(self):
        return "Family values"

# Intermediate class 
class Parent(Grandparent):
    def responsibility(self):
        return "Taking care of children"

# Child class 
class Child(Parent):
    def play(self):
        return "Playing games"

# Example usage
c = Child()
print(c.legacy())         # From Grandparent
print(c.responsibility()) # From Parent
print(c.play())           # From Child
