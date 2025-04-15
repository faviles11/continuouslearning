def miniZigZag(arr):
    arr.sort()
    n = len(arr)
    mid = (n+1)//2-1
    arr[mid], arr[-1] = arr[-1], arr[mid]
    arr[mid+1:] = arr[mid+1:][::-1]
    return arr




# Ejemplo de uso:
print(miniZigZag([4, 3, 7, 8, 6, 2, 1]))
