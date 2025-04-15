def plusminus(arr):
    new_arr = []
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for n in arr:
        if n > 0:
            count_pos += 1
        elif n < 0:
            count_neg += 1
        else:
            count_zero += 1
    print(f"{count_pos / len(arr):.6f}")
    print(f"{count_neg / len(arr):.6f}")
    print(f"{count_zero / len(arr):.6f}")

arr = [1, 1, 0, -1, -1]
print(plusminus(arr))