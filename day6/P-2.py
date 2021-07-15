x=int(input())
a=[0 for _ in range(x+1)] #a=[none]*(x+1)
a[1]=0

for i in range(2,x+1):
    a[i]=a[i-1]+1
    if i%5==0:
        a[i]=min(a[i//5]+1,a[i])
    if i%3==0:
        a[i]=min(a[i//3]+1,a[i])
    if i%2==0:
        a[i]=min(a[i//2]+1,a[i])
        
print(a[x])