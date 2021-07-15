arr=list(map(int, input().split()))
plus=1
plus_temp=1
miner=1
miner_temp=1
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        plus+=1
        if plus > plus_temp:
            plus_temp=plus
        miner=1
    elif arr[i] > arr[i+1]:
        miner+=1
        if miner > miner_temp:
            miner_temp=miner
        plus=1
    else:
        plus=1
        miner=1
print('%d %d' %(plus_temp,miner_temp))