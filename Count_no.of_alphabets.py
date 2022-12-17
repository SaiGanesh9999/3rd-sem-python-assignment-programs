s = input()
n = len(s)
c=0
for i in range(n):
    if s[i].isalpha()==1:
        c=c+1
print(c)
