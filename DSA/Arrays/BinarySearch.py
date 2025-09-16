def BinarySearch(arr,value):
    low = 0
    high = len(arr) - 1 
    
    while low <= high:
        mid = (high+low)//2
        if value == arr[mid]:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [20,35,37,40,45,56,65,71,78]
value = 37
index = BinarySearch(arr,value)
print("Found the num at index:", index)