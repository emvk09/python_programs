hr=input('Enter the hours worked:')
rp=input('Enter the rate per hour:')
def computepay():
    if float(hr)<=40:
        b=float(hr)*float(rp)
        return b
    else:
        c=(float(hr)-40)*1.5*float(rp)+(40*float(rp))
        return c
print('Pay',computepay())
