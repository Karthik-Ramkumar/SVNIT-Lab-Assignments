import hashlib

# Get the original message
message = input("Enter the original message: ")

# Generate original message digests
md5_hash = hashlib.md5(message.encode()).hexdigest()
sha1_hash = hashlib.sha1(message.encode()).hexdigest()
sha256_hash = hashlib.sha256(message.encode()).hexdigest()

print("\nOriginal Message:", message)
print("MD5:    ", md5_hash)
print("SHA-1:  ", sha1_hash)
print("SHA-256:", sha256_hash)

# Get the received or modified message
received = input("\nEnter the received message: ")

# Select hashing algorithm
print("\n1. MD5")
print("2. SHA-1")
print("3. SHA-256")

choice = input("Select algorithm (1/2/3): ")

if choice == "1":
    original_digest = hashlib.md5(message.encode()).hexdigest()
    received_digest = hashlib.md5(received.encode()).hexdigest()
elif choice == "2":
    original_digest = hashlib.sha1(message.encode()).hexdigest()
    received_digest = hashlib.sha1(received.encode()).hexdigest()
elif choice == "3":
    original_digest = hashlib.sha256(message.encode()).hexdigest()
    received_digest = hashlib.sha256(received.encode()).hexdigest()
else:
    print("Invalid choice")
    exit()

# Compare digests
print("\nReceived Message:", received)
print("Received Digest:", received_digest)

if original_digest == received_digest:
    print("Integrity Verified: Message is unchanged.")
else:
    print("Integrity Failed: Message has been modified.")
