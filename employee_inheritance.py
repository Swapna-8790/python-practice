class Person:
    def display(self):
        print("person class")
class Employee(Person):
    def work(self):
        print("employee working")
e=Employee()
e.display()
e.work()