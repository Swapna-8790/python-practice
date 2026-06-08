text=input("enter a sentence: ")
words=text.split()
unique_words=set(words)
for i in unique_words:
    print(i,"=",words.count(i))
