s = input()
n = len(s)
c=0
for i in range(n):
    if s[i].isdigit()==1:
        c=c+1
print(c)
