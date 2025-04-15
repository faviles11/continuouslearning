def addarr(arr):
    adder = 0
    for n in arr:   
        adder += n
    return adder

def addarr2(arr):
    return sum(arr)

arr = [1,2,2]

print(addarr(arr))
print(addarr2(arr))