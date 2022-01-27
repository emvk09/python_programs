snsf=None
print('Before:',snsf)
for i in [45,66,15,4,1,55,6,55,555,58,54,5,55855,5,585,57]:
    if snsf==None:
        snsf=i
    elif i<snsf:
        snsf=i
    print(i,', Smallest number so far:',snsf)
print('After:',snsf)
