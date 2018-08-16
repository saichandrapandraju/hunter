a=input()
temp=a
for i in range(97,123):
    a=a.replace(chr(i),'')
    if(a==a[::-1]):
        print('YES')
        break
    a=temp
    if(i==122):
        print('NO')
    
