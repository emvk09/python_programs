small=None
largest=None
while True:
    inp=input('Enter the integer numbers: ')
    if inp=='done':
        break
    try:
        cinp=int(inp)
    except:
        print('Invalid input')
    if  small==None:
        small=cinp
    elif cinp<small:
        small=cinp
    elif largest==None:
        largest=cinp
    elif cinp>largest:
        largest=cinp
print('Maximum is',largest)
print('Minimum is',small)
