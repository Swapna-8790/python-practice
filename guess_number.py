import random
secret=random.randint(1,10)
guess=int(input("guess a number from 1 to 10: "))
if guess==secret:
    print("correct")
else:
    print("wrong")
    print("number was",secret)