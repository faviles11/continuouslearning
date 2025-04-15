def m(arr):
    arr.sort()
    min = sum(arr[:-1])
    max = sum(arr[1:])
    return min, max

arr = [1,3,5,7,9]

print(m(arr))