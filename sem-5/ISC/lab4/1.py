# Playfair Cipher

key = "DRONE"
plaintext = "ATTACK AT THE STATION"

# Create 5 x5 Key Matrix

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is removed

key = key.upper().replace("J", "I")

# Remove duplicate letters from key
letters = ""
for ch in key:
    if ch not in letters:
        letters += ch

# Add remaining alphabet
for ch in alphabet:
    if ch not in letters:
        letters += ch

#  5x5 matrix
matrix = []
for i in range(0, 25, 5):
    matrix.append(list(letters[i:i+5]))

print("Key Matrix:")
for row in matrix:
    print(row)

text = plaintext.replace(" ", "").upper().replace("J", "I")

pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        pairs.append(a + "X")
        i += 1

    elif text[i] == text[i + 1]:
        pairs.append(a + "X")
        i += 1

    else:
        pairs.append(a + text[i + 1])
        i += 2

print("\nDigraphs:")
print(pairs)


# to find position
def position(letter):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == letter:
                return r, c

def encrypt_pair(pair):
    a, b = pair

    r1, c1 = position(a)
    r2, c2 = position(b)

    # Same row
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + \
               matrix[r2][(c2 + 1) % 5]

    # Same column
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + \
               matrix[(r2 + 1) % 5][c2]

    # Rectangle
    else:
        return matrix[r1][c2] + matrix[r2][c1]


ciphertext = ""

for pair in pairs:
    ciphertext += encrypt_pair(pair)

print("\nCiphertext:")
print(ciphertext)


def decrypt_pair(pair):
    a, b = pair

    r1, c1 = position(a)
    r2, c2 = position(b)

    # Same row
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + \
               matrix[r2][(c2 - 1) % 5]

    # Same column
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + \
               matrix[(r2 - 1) % 5][c2]

    # Rectangle
    else:
        return matrix[r1][c2] + matrix[r2][c1]


decrypted = ""

for i in range(0, len(ciphertext), 2):
    decrypted += decrypt_pair(ciphertext[i:i+2])

print("\nDecrypted:")
print(decrypted)