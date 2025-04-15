def li(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return None
arr = [1, 2, 3, 4, 3, 2, 1]
result = li(arr)
print(result)