try:
    num=int(input("enter first number: "))
    print(num)
except ValueError:
    print("invalid input")
finally:
    print("program finished")