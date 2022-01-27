print("Welcome to EDWIN'S calculator")
while True:
    num=input('Enter the numbers: ')
    if num=='done':
        break
    try:
        nums=int(num)
    except:
        print('Invalid Input. Please enter numbers only.')
