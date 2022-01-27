text='X-DSPAM-Confidence:    0.8475'
spal=text.find('0')
sspal=text[spal:spal+6]
print (float(sspal))
