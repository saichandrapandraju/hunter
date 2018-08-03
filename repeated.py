a=raw_input()
c=len(a)
q=0
w=0
new=[]
list=[int(x) for x in raw_input().split()]
while(q==0):
    l=list[q]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        print l,
        new.insert(w,l)
        w+=1
    elif((list==new)and(l not in new)):
        print('unique')
    else:
        q=0
    if(list==[]):
        break
