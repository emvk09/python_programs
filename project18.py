dir=list()
while True:
    nrom=input('Enter the file name:\n')
    try:
        srom=open(nrom)
        break
    except:
        print("The file name you entered doesn't exsist.\nPlease enter a valid file name.")
for line in srom:
    z=line.split()
    for c in z:
        if c in dir:
            continue
        else:
            dir.append(c)
dir.sort()
print(dir)
