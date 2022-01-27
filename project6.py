sc=input('Enter your score between 0.0 and 1.0: ')
try:
    asc=float(sc)
except:
    asc=-1
if asc>=1:
    print('Error')
elif asc>=0.9:
    print('A')
elif asc>=0.8:
    print('B')
elif asc>=0.7:
    print('C')
elif asc>=0.6:
    print('D')
elif asc==-1.0:
    print('Enter the score only and donot enter the any other characters.')
else:
    print('E')
