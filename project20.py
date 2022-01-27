dic=dict()
lis=list()
print('\nEnter the names to know the number of times they are repeated.\nAfter you finish entering the names please type "done" to get the result.\n')
while True:
    nam=input()
    snam=nam.strip()
    if snam=='done': break                                  #we can also write:
    lis.append(snam)                                        #if snam=='done':
for name in lis:                                            #    break
    if name in dic:
        dic[name]=dic[name]+1
    else:                                                    #we can also do this using GET METHOD
        dic[name]=1                                          #refer project21
print(dic)
