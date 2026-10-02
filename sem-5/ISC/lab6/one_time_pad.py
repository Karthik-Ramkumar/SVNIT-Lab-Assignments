import random
import string

# Plaintext and random key generation
plaintext = "HELLO WORLD"
text = plaintext.replace(" ", "").upper()
key = [random.randint(0, 25) for _ in range(len(text))]

print(f"Plaintext:  {text}")
print(f"Key:        {key}")

# Encrypt: C = (P + K) mod 26
ciphertext = "".join(chr((ord(c) - ord('A') + k) % 26 + ord('A')) for c, k in zip(text, key))
print(f"Ciphertext: {ciphertext}")

# Decrypt: P = (C - K) mod 26
decrypted = "".join(chr((ord(c) - ord('A') - k) % 26 + ord('A')) for c, k in zip(ciphertext, key))
print(f"Decrypted:  {decrypted}")
print(f"Original plaintext recovered: {decrypted == text}")
