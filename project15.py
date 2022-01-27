fnam=input('Enter the file name: ')
count=0
tot=0
try:
    snam=open(fnam)
except:
    print("The given file name",fnam,"doesn't exist.")
    quit()
for line in snam:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        aline=line.find(':')
        bline=line[aline+1:]
        bline=bline.lstrip()
        cline=float(bline)
        tot=cline+tot
avg=tot/count
print('Average spam confidence:',avg)
