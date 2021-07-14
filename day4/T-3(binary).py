
import math
def BinarySearch(lst,key,N):
    high=high_arr-(math.ceil(M/N))
    low=high_arr-M
    while low <= high:
        mid=(low+high)//2
        sum=0
        for i in lst:
            if i > mid:
                cut=i-mid
                sum+=cut
        if key > sum:
            high=mid-1
        else: #최대한 덜 짤랐을떄가 답이므로 여기서 계속 저장해둠
            answer=mid
            low=mid+1
    return answer
           
N,M=map(int,input().split())
arr=list(map(int, input().split()))
high_arr=max(arr)
print(BinarySearch(arr,M,N))