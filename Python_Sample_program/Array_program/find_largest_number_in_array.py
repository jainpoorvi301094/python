def largest_number(arr, n):
    max=arr[0]
    for i in range(1, n):
        if arr[i]>max:
            max= arr[i]
    return max

arr=[1,5,7,2,9]
n= len(arr)
print(largest_number(arr,n))

