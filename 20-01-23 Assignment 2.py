s = input()
vowels = ['a','e','i','o','u']
for i in s:
    if i in vowels:
        s = s.replace(i,'')
#remove is list method so used replace for string 
print(s)
