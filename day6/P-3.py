from typing import Text


x,y=map(int,input().split())
arr=[]
two_index=[]
for i in range(x):
    b=list(map(int,input().split()))
    arr.append(b)
    for j in range(y):
        if arr[i][j]==2:
            two_index.append([i,j])
n=int(input())
count=0
cnt_min=100000
k=-1
p=0
while p < (x-n):
    flag=True
    k+=1
    cnt=0
    if k > (x-n) :
        p+=1
        k=0
    for i in range(k,n+k):
        if flag==False:
            break
        for j in range(p,n+p):
            if arr[i][j] == 1:
                cnt+=1
            elif [i,j] in two_index:
                flag=False
                break
    if flag == True and cnt < cnt_min:
        cnt_min=cnt

if cnt_min==100000:
    print('-1')
else:
    print(cnt_min)



    
