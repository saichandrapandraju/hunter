m=int(input())
l=[int(x) for x in input().split()]
k=l[::-1]
for i in range(0,m):
	if(i+1<m):
		print(k[i],end='->')
	else:
		print(k[i])
