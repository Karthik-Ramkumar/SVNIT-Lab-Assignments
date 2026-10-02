import numpy as np

K = np.array([[3, 3], [2, 5]])
plaintext = "MEET AT BASE"

# Prepare plaintext: 
text = plaintext.replace(" ", "").upper()
if len(text) % 2 != 0:
    text += "X"

print("Key Matrix K:")
print(K)

# Map letters to numbers and split into 2-letter blocks
nums = [ord(c) - ord('A') for c in text]
blocks = [nums[i:i+2] for i in range(0, len(nums), 2)]
print(f"\nPlaintext: {text}")
print(f"Blocks: {[''.join(text[i:i+2]) for i in range(0, len(text), 2)]}")

# Encrypt each block: C = K * P mod 26
encrypted_blocks = []
ciphertext = ""
for block in blocks:
    p = np.array(block)
    c = K @ p % 26
    encrypted_blocks.append(c.tolist())
    ciphertext += "".join(chr(v + ord('A')) for v in c)

print(f"\nEncrypted numerical blocks: {encrypted_blocks}")
print(f"Ciphertext: {ciphertext}")

# Modular inverse of K mod 26 using determinant method
det = int(round(np.linalg.det(K))) % 26
# Find modular inverse of determinant mod 26
det_inv = None
for i in range(26):
    if (det * i) % 26 == 1:
        det_inv = i
        break

# Adjugate of 2x2 matrix [[a,b],[c,d]] is [[d,-b],[-c,a]]
adj = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])
K_inv = (det_inv * adj) % 26

print(f"\nDeterminant of K mod 26: {det}")
print(f"Modular inverse of det: {det_inv}")
print(f"Inverse Key Matrix K_inv:\n{K_inv}")

# Decrypt each block: P = K_inv * C mod 26
decrypted = ""
for c_block in encrypted_blocks:
    c = np.array(c_block)
    p = K_inv @ c % 26
    decrypted += "".join(chr(int(v) + ord('A')) for v in p)

print(f"\nDecrypted text: {decrypted}")
print(f"Original plaintext recovered: {decrypted == text}")
