s = k = input()
ans = ''
for i in s:
    if i not in ans:
        ans+=str(s.count(i))+i
        s = s.replace(i,'')
print(ans)
