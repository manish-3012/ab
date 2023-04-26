# Import the required libraries
from math import pow

# Define the prime number and generator
prime_number = 23
generator = 5

# Alice's private key
alice_private_key = 6

# Bob's private key
bob_private_key = 15

# Calculate Alice's public key
alice_public_key = pow(generator, alice_private_key) % prime_number

# Calculate Bob's public key
bob_public_key = pow(generator, bob_private_key) % prime_number

# Calculate the shared secret key
alice_shared_secret_key = pow(bob_public_key, alice_private_key) % prime_number
bob_shared_secret_key = pow(alice_public_key, bob_private_key) % prime_number

# Print the results
print("Alice's private key:", alice_private_key)
print("Bob's private key:", bob_private_key)
print("Alice's public key:", alice_public_key)
print("Bob's public key:", bob_public_key)
print("Shared secret key (Alice's perspective):", alice_shared_secret_key)
print("Shared secret key (Bob's perspective):", bob_shared_secret_key)
