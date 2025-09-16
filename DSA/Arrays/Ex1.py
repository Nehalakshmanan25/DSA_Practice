arr = [1,3,4,5,None]
pos=1
val=2
for i in range(len(arr) - 2, pos-1,-1):
    arr[i+1] = arr[i]
arr[pos]=val
print(arr)