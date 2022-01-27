num=list()
while True:
    cin=input('Enter the numbers:')
    if cin=='done':
        break
    try:
        fcin=float(cin)
        num.append(fcin)
    except:
        print('Invalid input')
        continue
print('The average is: ',sum(num)/len(num))
