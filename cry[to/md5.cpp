#include <iostream>
#include <string>
#include <cstring>
#include <openssl/md5.h>
#include <openssl/aes.h>
using namespace std;

unsigned char* md5_digest(string input) {
    unsigned char* digest = new unsigned char[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)input.c_str(), input.length(), digest);
    return digest;
}

unsigned char* aes_encrypt(string input, unsigned char* key, unsigned char* iv) {
    unsigned char* output = new unsigned char[input.length() + AES_BLOCK_SIZE];
    int output_length;
    AES_KEY aes_key;
    AES_set_encrypt_key(key, 128, &aes_key);
    AES_cbc_encrypt((unsigned char*)input.c_str(), output, input.length(), &aes_key, iv, AES_ENCRYPT);
    return output;
}

unsigned char* aes_decrypt(unsigned char* input, int input_length, unsigned char* key, unsigned char* iv) {
    unsigned char* output = new unsigned char[input_length];
    int output_length;
    AES_KEY aes_key;
    AES_set_decrypt_key(key, 128, &aes_key);
    AES_cbc_encrypt(input, output, input_length, &aes_key, iv, AES_DECRYPT);
    return output;
}

int main() {
    string passphrase = "My super secret passphrase";
    string message = "Hello, world!";
    
    // Derive key from passphrase using MD5
    unsigned char* key = md5_digest(passphrase);
    unsigned char iv[AES_BLOCK_SIZE] = {0};
    
    // Encrypt message using AES with derived key
    unsigned char* encrypted = aes_encrypt(message, key, iv);
    int encrypted_length = message.length() + AES_BLOCK_SIZE;
    
    // Decrypt message using AES with derived key
    unsigned char* decrypted = aes_decrypt(encrypted, encrypted_length, key, iv);
    
    // Print original message and decrypted message to confirm correctness
    cout << "Original message: " << message << endl;
    cout << "Decrypted message: " << decrypted << endl;
    
    // Clean up allocated memory
    delete[] key;
    delete[] encrypted;
    delete[] decrypted;
    
    return 0;
}
