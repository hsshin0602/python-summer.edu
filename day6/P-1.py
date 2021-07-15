cost=int(input())
arr=list(map(int,input().split()))
sum=0
cnt=0
n=0
cnt_temp=0
while n < (len(arr)-1):
    for i in range(n,len(arr)-1):
        if sum+arr[i]<cost:
            sum+=arr[i]
            cnt+=1
        else:
            if cnt > cnt_temp:
                cnt_temp = cnt 
    cnt=0
    sum=0  
    n+=1
print(cnt_temp)