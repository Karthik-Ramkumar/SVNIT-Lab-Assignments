import math

# Affine cipher parameters: y = (a*x + b) mod 26, gcd(a, 26) must be 1
a, b = 5, 8
plaintext = "HELLO WORLD"
text = plaintext.replace(" ", "").upper()

print(f"Plaintext:  {text}")
print(f"Key: a={a}, b={b}")

# Encrypt: y = (a * x + b) mod 26
ciphertext = "".join(chr((a * (ord(c) - ord('A')) + b) % 26 + ord('A')) for c in text)
print(f"Ciphertext: {ciphertext}")

# Find modular inverse of a mod 26 for decryption
a_inv = next(i for i in range(26) if (a * i) % 26 == 1)
print(f"Modular inverse of a ({a}) mod 26: {a_inv}")

# Decrypt: x = a_inv * (y - b) mod 26
decrypted = "".join(chr((a_inv * (ord(c) - ord('A') - b)) % 26 + ord('A')) for c in ciphertext)
print(f"Decrypted:  {decrypted}")
print(f"Original plaintext recovered: {decrypted == text}")
