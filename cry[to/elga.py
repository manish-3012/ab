import random

# Generate a large prime number
def generate_prime_number():
    while True:
        p = random.randint(100000, 200000)
        if is_prime(p):
            return p

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Compute the modular inverse of a number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Generate a public/private key pair
def generate_key_pair():
    # Generate a large prime number
    p = generate_prime_number()

    # Choose a random number g that is a primitive root modulo p
    while True:
        g = random.randint(2, p - 1)
        if pow(g, (p - 
