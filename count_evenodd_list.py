numbers=[10,15,22,33,40]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)