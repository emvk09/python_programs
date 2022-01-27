filename=input('Enter the required file name: ')
try:
    subfile=open(filename)
except:
    print("The entered file name",filename,"doesn't exist.")
    quit()
for line in subfile:
    line=line.rstrip()
    line=line.upper()
    print (line)
