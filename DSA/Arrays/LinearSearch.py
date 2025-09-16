def LinearSearch(arr,value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

arr = [1,2,3,4,5]
value = 4

result = LinearSearch(arr,value)
print(result)