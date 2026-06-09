class Mobile:
    def __init__(self,company):
        self.company=company
    def display(self):
        print("company:",self.company)
m=Mobile("samsung")
m.display()