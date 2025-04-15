def super_digit(n, k):
    # Concatenate the string n, k times
    p = n * k
    # iterates until p is a single digit
    while(len(p)>1):
        total = 0
        for digit in p:
            total += int(digit)
        p = str(total)
    return int(p)

# Test cases
print(super_digit("9875", 4))  # Output: 8
print(super_digit("148", 3))   # Output: 3        
