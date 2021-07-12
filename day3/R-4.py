k=int(input())
a= list(map(int,input().split()))
if k > sum(a):
    answer=-1
else:
    b=[]
    for i in range(len(a)):
        b.append([a[i],i+1])
    b_len=len(b)
    m=min(a)
    while k>=m*b_len:
        k-=m*b_len 
        j=0
        while j < len(b): 
            b[j][0]-=m
            if b[j][0]==0:
                b.remove(b[j])
                j-=1
            j+=1     
        m=1000
        for i in b:
            if i[0]<m:
                m=i[0]
        b_len=len(b)
    answer=b[k%b_len][1]
    print(answer)
#시간복잡도는 O(최소값찾기 n+두번쨰 음식에서는 n-1 ''')
#k의 범위에 따라 시간복잡도가 달라짐-최악 n**2