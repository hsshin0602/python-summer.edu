a=list(map(int, input().split()))
p=0
m=0
x=[]
y=[]
z=[0,0]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        if p!=0:
            x.append(p+1)
            p=0
            m+=1
        else: #p==0
            if a[i+1]==-1:
                y.append(m+1)
            else:
                m+=1         
    elif a[i] < a[i+1]:
        if m!=0:
            y.append(m+1)
            m=0
            p+=1
        else: #m==0
            if a[i+1]==-1:
                x.append(p+1)
            else:
                p+=1 
    else:
        if p!=0 or m!=0:
            x.append(p+1)
            y.append(m+1)
            p=0
            m=0
if x:
    z[0]=max(x)
else:
    z[0]=1
if y:
    z[1]=max(y)
else:
    z[1]=1

if z[0]<=2:
    print('%d %d' %(1,z[1]))
elif z[1]<=2:
    print('%d %d' %(z[0],1))
else:
    print('%d %d' %(z[0],z[1]))

# 