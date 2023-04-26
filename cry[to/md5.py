import hashlib

# Define message to be hashed
message = "Hello, world!"

# Create a new hash object
hash_object = hashlib.md5()

# Update hash object with message
hash_object.update(message.encode('utf-8'))

# Get hexadecimal digest of hash
hash_hex = hash_object.hexdigest()

# Print hash value
print("Hash value of message:", hash_hex)
