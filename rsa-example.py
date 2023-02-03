# RSA key generation, encryption and decryption
# unoptimized implementation for educational purposes
# does not use libraries

# absolute value
def abs_value(x):
    if x < 0:
        return -x
    else:
        return x


# gcd(int1, int2) returns the greatest common divisor of the two integers int1 and int2.
# GCD is the largest common divisor that divides the numbers without a remainder.
def gcd(int1, int2):
    while int2 != 0:
        int1, int2 = int2, int1 % int2
    return abs_value(int1)


# Carmichael's λ function or reduced totient function
# for 2 prime numbers
def tote(p, q):
    return (p - 1) * (q - 1)


# e must be co-prime to tote λ(n) and
# smaller than tote λ(n).
def selectexponent(atote):
    e = 2
    while e < atote:
        if gcd(e, atote) == 1:
            break
        else:
            e = e + 1
    return e


# extended Euclidean algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x


# d ≡ e−1 (mod λ(n))
# d is the modular multiplicative inverse of e modulo λ(n)
# such that e*d % tote = 1
def selectprivate(e, atote):
    g, x, y = extended_gcd(e, atote)

    if g != 1:
        raise ValueError("modular inverse does not exist")
    else:
        return x % atote


class PrivateKey:
    def __init__(self, p=0, q=0):
        # p and q are large prime numbers,
        # should be chosen at random,
        # be similar in magnitude, but differ in length
        self.p = p
        self.q = q
        # n is used as the modulus for both the public and private keys
        # its length, usually expressed in bits, is the key length
        self.n = p * q
        # Carmichael's λ function or reduced totient function
        self.tote = int(tote(p, q))
        # choose an integer e so that e and tote λ(n) are coprime
        self.e = selectexponent(self.tote)
        # d ≡ e−1 (mod λ(n))
        # d is the modular multiplicative inverse of e modulo λ(n)
        self.d = selectprivate(self.e, self.tote)

    def print(self):
        print("// Choose two distinct prime numbers p and q.")
        print("privatekey p:", self.p)
        print("privatekey q:", self.q)
        print("\n// Calculate n = p * q.")
        print("privatekey n:", self.n)
        print("\n// Compute Euler's totient function tot(n) = φ(n) = (p - 1) * (q - 1)")
        print("privatekey tote:", self.tote)
        print("\n// Choose any number e where 1 < e < tot(n) and e is coprime to tot(n).")
        print("// Common choices are 3, 17, and 65537.")
        print("privatekey e:", self.e)
        print("\n// Compute d, the modular multiplicative inverse of e (mod tot(n)).")
        print("privatekey d:", self.d)


class PublicKey:
    def __init__(self, e=0, n=0):
        self.e = e
        self.n = n

    def print(self):
        print("publickey e:", self.e)
        print("publickey n:", self.n)


# cipher of number = (number to the power of e) modulo n
def encrypt(m, e, n):
    return (m ** e) % n


# number = (cipher to the power of d) module n
def decrypt(c, d, n):
    return (c ** d) % n


# Decrypt the message
    m = decrypt(c, d, n)
    return m

p_example = 22
q_example = 91

print("RSA key generation, encryption and decryption.")
print(f"p={p_example} and q={q_example} are hardcoded in the example.")

print("\nPrivate key:")
print("============")
private = PrivateKey(p_example, q_example)
private.print()
print("\nPublic key:")
print("===========")
public = PublicKey(private.e, private.n)
public.print()
message = 1234
message_cipher = encrypt(message, public.e, public.n)
message_decrypted = decrypt(message_cipher, private.d, public.n)
print(f"\nMessage: {message}")
print("\n// Encrypt using ciphertext(message) = m^e mod n")
print("// Both of these values must be integers 1 < m < n and 1 < c < n.")
print(f"Encrypted ciphertext: {message_cipher}")
print("\n// Decrypt using m(c) = c^d mod n.")
print(f"Decrypted message: {message_decrypted}")