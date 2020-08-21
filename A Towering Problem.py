result1=[]
sol=''
input1=list(map(int,input().split()))
a=input1[-2]
b=input1[-1]
input1.remove(a)
input1.remove(b)
input1.sort()
rev=input1[::-1]
i=0
x=0;y=1;z=2
while(i==0):
    res=rev[x]+rev[y]+rev[z]
    if(res==a):
        i=10
        sol=sol+str((rev[x]))+' '
        sol=sol+str((rev[y]))+' '
        sol=sol+str((rev[z]))+' '
        p=rev[x];q=rev[y];r=rev[z]
        rev.remove(p)
        rev.remove(q)
        rev.remove(r)
        rev.sort()
        rev1=rev[::-1]
        for i in rev1:
            sol=sol+str(i)+' '
    z=z+1
    if(z==6):
        y=y+1
        z=y+1
    if(y==5):
        x=x+1
        y=x+1
        z=y+1
    if(x==4 and y==5 and z==6):
        break
print(sol)
