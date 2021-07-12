n=int(input())
a=list(map(int,input().split()))
x=0
k=0
while k<n:
    for i in range(n):
        k+=1
        for j in range(n):
            if x >= a[2*j]:
                x+=a[2*j+1]
                a[2*j+1]=0
if x==0:
    print('-1')
else:
    print(x)
    