s=input()
l=[]
for i in s:
    l.append(int(i))
l.sort(reverse=True)
res=''
for i in l:
    res=res+str(i)
print(res)
