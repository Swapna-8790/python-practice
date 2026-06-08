try:
    a=int(input("enter first number: "))
    b=int(input("enter first number: "))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")