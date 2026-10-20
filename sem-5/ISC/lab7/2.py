
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Accept plaintext and secret key
plaintext = input("Enter plaintext: ")
key = input("Enter secret key (8 characters): ").encode()

if len(key) != 8:
    print("Error: DES key must be exactly 8 bytes.")
    exit()

# Convert plaintext to bytes
plaintext_bytes = plaintext.encode()

# Encryption
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext_bytes, DES.block_size))

# Display ciphertext
encoded_ciphertext = base64.b64encode(ciphertext).decode()
print("Ciphertext:", encoded_ciphertext)

# Decryption using the same key
cipher = DES.new(key, DES.MODE_ECB)
decoded_ciphertext = base64.b64decode(encoded_ciphertext)
decrypted_text = unpad(
    cipher.decrypt(decoded_ciphertext),
    DES.block_size
).decode()

print("Decrypted plaintext:", decrypted_text)

# Verify the result
if plaintext == decrypted_text:
    print("Verification: Successful")
else:
    print("Verification: Failed")
