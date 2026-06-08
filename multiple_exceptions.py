try:
    a=int(input("enter first number: "))
    b=int(input("enter first number: "))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Input")