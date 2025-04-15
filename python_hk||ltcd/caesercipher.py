def caesercipher(s,k):
    result = ""
    for char in s:
        if char.isupper():
            result += chr((ord(char) + k-65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += char
    return result