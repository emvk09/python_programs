hr=input('Enter the hours worked:')
rp=input('Enter the rate per hour:')
if float(hr)<=40:
    print(float(hr)*float(rp))
else:
    print((float(hr)-40)*1.5*float(rp)+(40*float(rp)))
