# python-rsa-example

RSA key generation, encryption and decryption

unoptimized implementation for educational purposes

does not use libraries

## Output

```
RSA key generation, encryption and decryption.
p=22 and q=91 are hardcoded in the example.

Private key:
============
// Choose two distinct prime numbers p and q.
privatekey p: 22
privatekey q: 91

// Calculate n = p * q.
privatekey n: 2002

// Compute Euler's totient function tot(n) = φ(n) = (p - 1) * (q - 1)
privatekey tote: 1890

// Choose any number e where 1 < e < tot(n) and e is coprime to tot(n).
// Common choices are 3, 17, and 65537.
privatekey e: 11

// Compute d, the modular multiplicative inverse of e (mod tot(n)).
privatekey d: 1031

Public key:
===========
publickey e: 11
publickey n: 2002

Message: 1234

// Encrypt using ciphertext(message) = m^e mod n
// Both of these values must be integers 1 < m < n and 1 < c < n.
Encrypted ciphertext: 662

// Decrypt using m(c) = c^d mod n.
Decrypted message: 1234
```
