count=0
while True:                                                                #refer project15 for some comparison
    fnam=input('Enter the file name:\n')
    try:
        snam=open(fnam)
        break
    except:
        print("The file name you entered doesn't exist.\nPlease enter a valid file name.")
for line in snam:
    if not line.startswith('From '): continue
    x=line.split()
    y=x[1]
    count=count+1
    print(y)
print('There were',count,'lines in the file with From as the first word')
