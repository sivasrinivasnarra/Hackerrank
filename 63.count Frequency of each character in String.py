x=input('Input String:\n')
res={}
for i in x:
    if i not in res:
        res[i]=1
    else:
        res[i]+=1
print('Count of all characters are:')
for k,v in res.items():
    print(k,'-->',v)