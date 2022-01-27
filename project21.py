dic=dict()
lis=list()
print('\nEnter the names:\n')
while True:
    nam=input()
    snam=nam.strip()
    if snam=='done': break
    lis.append(snam)
for name in lis:
    if name in dic:
        dic[name]=dic[name]+1
    else:
        dic[name]=1
print(dic)
