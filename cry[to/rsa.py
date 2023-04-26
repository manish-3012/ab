import random

# Generate two prime numbers p and q
def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

def is_prime(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False
    else:
        return True

p = generate_prime_number()
q = generate_prime_number()

# Calculate n and phi(n)
n = p*q
phi = (p-1)*(q-1)

# Choose e such that 1 < e < phi and e is coprime with phi
def choose_e(phi):
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            return i

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

e = choose_e(phi)

# Calculate d such that d*e = 1 mod phi
def choose_d(e, phi):
    d = 0
    while True:
        d += 1
        if (d*e) % phi == 1:
            return d

d = choose_d(e, phi)

# Encrypt and decrypt messages
def encrypt(message):
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

def decrypt(cipher):
    message = [chr((char ** d) % n) for char in cipher]
    return ''.join(message)

# Example usage
message = "Hello, world!"
cipher = encrypt(message)
print("Encrypted message:", cipher)
decrypted_message = decrypt(cipher)
print("Decrypted message:", decrypted_message)
