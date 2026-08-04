def encrypt(text, shift):
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

text = input("Enter text: ")
shift = int(input("Enter shift: "))

cipher = encrypt(text, shift)
print("Encrypted:", cipher)

plain = decrypt(cipher, shift)
print("Decrypted:", plain)