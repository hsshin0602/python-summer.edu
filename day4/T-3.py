n,m=map(int, input().split())
a=list(map(int, input().split()))
x=0
b=[]
while m>=x:
    for i in range(n):
        a_max=max(a)
        if a[i]==a_max:
            a[i]-=1
            x+=1
print(max(a))

# h-m,h-m/n 범위내에서 이진탐색