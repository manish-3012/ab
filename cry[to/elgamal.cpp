#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

int mod_pow(int base, int exponent, int modulus) {
    int result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = (result * base) % modulus;
        }
        base = (base * base) % modulus;
        exponent = exponent / 2;
    }
    return result;
}

int main() {
    // Generate prime number and generator
    int p = 2147483647; // large prime number
    int g = 5; // primitive root modulo p
    
    // Generate private key
    srand(time(0));
    int x = rand() % (p-2) + 1;
    
    // Compute public key
    int y = mod_pow(g, x, p);
    
    // Print keys
    cout << "Private key x: " << x << endl;
    cout << "Public key (p, g, y): (" << p << ", " << g << ", " << y << ")" << endl;
    
    // Encrypt message
    int m = 12345; // plaintext message
    srand(time(0));
    int k = rand() % (p-2) + 1; // random secret key
    int a = mod_pow(g, k, p);
    int b = (m * mod_pow(y, k, p)) % p;
    
    // Print ciphertext
    cout << "Plaintext message: " << m << endl;
    cout << "Ciphertext (a, b): (" << a << ", " << b << ")" << endl;
    
    // Decrypt ciphertext
    int m_prime = (b * mod_pow(a, p-1-x, p)) % p;
    
    // Print decrypted message
    cout << "Decrypted message: " << m_prime << endl;
    
    return 0;
}
