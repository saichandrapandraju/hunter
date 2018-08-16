n=int(raw_input())
new=[]
list=[int(x) for x in raw_input().split()]
for i in range(0,n):
	if(i==list[i]):
		new.append(i)
	elif((new==[]) and (i==(n-1))):
		print('-1')
s=sorted(new)
k=len(s)
for i in range(0,k):
	print s[i],
		
