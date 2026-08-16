def brute_force_caesar(ciphertext):
    for shift in range(1, 26):
        decrypted = ""

        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char

        print(f"Shift {shift}: {decrypted}")


# Example
ciphertext1 = input("Enter text to encrypt: \n")
ciphertext = "SDWLHQW-9842"
brute_force_caesar(ciphertext1)