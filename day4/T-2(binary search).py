def BinarySearchR(lst, key, N):
    low=0
    high=N-1
    while True:
        mid=(low+high)//2
        if(low > high):
            if(lst[mid]==key):
                return mid
            else: 
                return mid+1
        elif lst[mid] < key:
            low = mid+1
        elif lst[mid] >= key:
            high = mid-1

def BinarySearchL(lst,key,N):
    low=0
    high=N-1
    while True:
        mid=(low+high)//2
        if low>high:
            if lst[mid]==key:
                return mid
            else:
                return mid-1
        elif lst[mid] <= key:
            low=mid+1
        elif lst[mid] > key:
            high=mid-1


N,x=map(int,input().split())
arr=list(map(int,input().split()))
low_index=BinarySearchR(arr,x,N)
high_index=BinarySearchL(arr,x,N)
if low_index:
    print(high_index-low_index+1)
else:
    print('-1')