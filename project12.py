word=input('Enter the word for which you want to count the number of times "a" is repeated : ')
start=0
for i in word:
    if i=='a':
        start=start+1
print(start)
