def comparetriplets(arr1,arr2):
    score1 = 0
    score2 = 0
    for n in range(len(arr1)):
        if arr1[n] > arr2[n]:
            score1 += 1
        elif arr1[n] < arr2[n]:
            score2 += 1
    print(score1, score2)

def comparetriplest2(arr1, arr2):
    score1 = 0
    score2 = 0
    for a, b in zip(arr1,arr2):
        if a > b:
            score1 += 1
        elif a < b:
            score2 += 1
    return score1, score2        

arr1 = [1, 3, 3]
arr2 = [3, 2, 1]
print(comparetriplets(arr1, arr2))
print(comparetriplest2(arr1, arr2))