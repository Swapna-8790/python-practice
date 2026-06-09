class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("student name:",self.name)
s1=Student("swapna")
s1.display()