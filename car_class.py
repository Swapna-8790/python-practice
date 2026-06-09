class Car:
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        print("car brand:",self.brand)
c=Car("Tayota")
c.show()