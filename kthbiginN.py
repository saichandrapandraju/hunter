n,k=map(int,input().split())
l=[int(x) for x in input().split()]
s=sorted(l)
print(s[n-k])
