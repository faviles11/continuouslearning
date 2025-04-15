def staircase(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        hashes = "#" * (i + 1)
        print(spaces + hashes)

staircase(6)
