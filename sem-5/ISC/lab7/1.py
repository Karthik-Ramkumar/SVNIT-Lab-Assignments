# Data Encryption Standard (DES) Implementation in Pure Python

# 1. Initial Permutation (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# 2. Final Permutation (IP Inverse / FP)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# 3. Expansion Table (E)
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# 4. Permutation Table (P)
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# 5. Permuted Choice 1 (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# 6. Permuted Choice 2 (PC-2)
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# 7. Key schedule shifts for 16 rounds
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 8. S-Boxes (S1 through S8)
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


def permute(bits, table):
    """Permute bits according to a given 1-indexed permutation table."""
    return "".join(bits[i - 1] for i in table)


def left_shift(bits, n):
    """Circular left shift a bit string by n positions."""
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    """Bitwise XOR between two bit strings of equal length."""
    return "".join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))


def generate_round_keys(key_bits):
    """Generate 16 subkeys (each 48 bits) from a 64-bit key."""
    # Apply PC-1: 64 bits -> 56 bits (C0: 28 bits, D0: 28 bits)
    key_56 = permute(key_bits, PC1)
    C = key_56[:28]
    D = key_56[28:]

    round_keys = []
    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        # Apply PC-2: 56 bits -> 48 bits
        round_keys.append(permute(C + D, PC2))

    return round_keys


def feistel_function(R, round_key):
    """Feistel round function f(R, K)."""
    # 1. Expand 32-bit R to 48 bits using table E
    expanded_R = permute(R, E)

    # 2. XOR with 48-bit round key
    xored = xor(expanded_R, round_key)

    # 3. S-box substitution (8 groups of 6 bits -> 8 groups of 4 bits = 32 bits)
    s_output = ""
    for i in range(8):
        block = xored[i * 6:(i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOXES[i][row][col]
        s_output += f"{val:04b}"

    # 4. Straight permutation P (32 bits -> 32 bits)
    return permute(s_output, P)


def des_process_block(block_bits, round_keys):
    """Encrypt/Decrypt a single 64-bit block through 16 Feistel rounds."""
    # Initial Permutation (IP)
    permuted = permute(block_bits, IP)
    L = permuted[:32]
    R = permuted[32:]

    # 16 Feistel Rounds
    for rk in round_keys:
        next_L = R
        next_R = xor(L, feistel_function(R, rk))
        L, R = next_L, next_R

    # Pre-output: swap R16 and L16
    pre_output = R + L

    # Final Permutation (FP / IP^-1)
    return permute(pre_output, FP)


def pad_pkcs7(data):
    """Pad byte sequence to a multiple of 8 bytes using PKCS#7."""
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)


def unpad_pkcs7(padded_data):
    """Remove PKCS#7 padding from decrypted byte sequence."""
    pad_len = padded_data[-1]
    if pad_len < 1 or pad_len > 8:
        return padded_data
    return padded_data[:-pad_len]


def prepare_key_bits(key_str):
    """Convert key string into 64-bit binary representation (8 bytes)."""
    key_bytes = key_str.encode('utf-8')
    if len(key_bytes) < 8:
        # Pad with spaces if less than 8 characters
        key_bytes = key_bytes.ljust(8, b' ')
    else:
        # Take first 8 bytes if longer
        key_bytes = key_bytes[:8]
    return "".join(f"{b:08b}" for b in key_bytes)


def des_encrypt(plaintext, key_str):
    """Encrypt a plaintext string using DES."""
    key_bits = prepare_key_bits(key_str)
    round_keys = generate_round_keys(key_bits)

    # Pad plaintext bytes to multiple of 8 bytes
    data_bytes = pad_pkcs7(plaintext.encode('utf-8'))
    data_bits = "".join(f"{b:08b}" for b in data_bytes)

    cipher_bits = ""
    for i in range(0, len(data_bits), 64):
        block = data_bits[i:i + 64]
        cipher_bits += des_process_block(block, round_keys)

    # Convert binary to hex representation
    cipher_bytes = bytes(int(cipher_bits[i:i + 8], 2) for i in range(0, len(cipher_bits), 8))
    return cipher_bytes.hex()


def des_decrypt(ciphertext_hex, key_str):
    """Decrypt a hexadecimal ciphertext string using DES."""
    key_bits = prepare_key_bits(key_str)
    # Decryption uses the same subkeys in reverse order
    round_keys = generate_round_keys(key_bits)[::-1]

    cipher_bytes = bytes.fromhex(ciphertext_hex)
    cipher_bits = "".join(f"{b:08b}" for b in cipher_bytes)

    recovered_bits = ""
    for i in range(0, len(cipher_bits), 64):
        block = cipher_bits[i:i + 64]
        recovered_bits += des_process_block(block, round_keys)

    plain_bytes = bytes(int(recovered_bits[i:i + 8], 2) for i in range(0, len(recovered_bits), 8))
    plain_bytes = unpad_pkcs7(plain_bytes)
    return plain_bytes.decode('utf-8', errors='replace')


def main():
    print("=" * 60)
    print("      DATA ENCRYPTION STANDARD (DES) ALGORITHM")
    print("=" * 60)

    # 1. Accept a plaintext message from the user
    plaintext = input("1. Enter plaintext message: ")

    # 2. Accept a secret key
    key = input("2. Enter secret key (8 characters): ")

    # 3. Encrypt the plaintext using DES
    ciphertext = des_encrypt(plaintext, key)

    # 4. Display the resulting ciphertext
    print(f"\n3. Encrypting plaintext using DES...")
    print(f"4. Ciphertext (Hexadecimal): {ciphertext}")

    # 5. Decrypt the ciphertext using the same key
    decrypted = des_decrypt(ciphertext, key)

    # 6. Display the recovered plaintext
    print(f"\n5. Decrypting ciphertext using the same key...")
    print(f"6. Recovered Plaintext: {decrypted}")

    # 7. Verify that decrypted plaintext is identical to original plaintext
    is_identical = (decrypted == plaintext)
    print(f"\n7. Verification:")
    print(f"   Original Plaintext  : '{plaintext}'")
    print(f"   Decrypted Plaintext : '{decrypted}'")
    print(f"   Identical Match     : {is_identical}")
    print("=" * 60)


if __name__ == "__main__":
    main()
