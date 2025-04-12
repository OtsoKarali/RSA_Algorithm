# Otso Karali, ret7qp, CS 3710, April 10th, 2025

import random

# written notes on RSA Algorithm : https://www.youtube.com/watch?v=4zahvcJ9glg&t=29s and https://www.youtube.com/watch?v=oOcTVTpUsPQ

# 1. Generate two arge prime numbers, p and q.
# 2. calculate the product n = p * q. This number n is used as the modulus for both the public and private keys.
# 3. calculate Euler's totient  phi(n) = (p-1) * (q-1).
# 4. choose a number e such that 1 < e < phi(n) and e is coprime to phi(n). This number e is the public exponent, or e for encryption.
# 5. determine d as d*e(mod(phi(n))) ≡ 1. This number is the private exponent, or d for decryption.
# 6. The public key is (e, n) and the privte key is (d, n).
# 7. to encrypt a message m, convert the message to a number m such that 0 <= m < n. The ciphertext c is calculated as c ≡ m^e (mod n).
# 8. To decrypt the cipertext c, compute m ≡ c^d (mod n). This will retrieve the original message m.


# logic directly from my time in CSO Last Semester
# Check if a number is prime
def is_prime(num):

    if num <= 1:
        return False

    # divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



# generate a random prime
def generate_prime(limit):
    while True:
        num = random.randint(2, limit)
        if is_prime(num):
            return num




# calculate the greatest common divisor- gcd
# again, logic from CSO last semester
def gcd(a, b):
    while b:
        # Store a as atemp
        temp = a
        # Set a to b
        a = b
        # Set b to a % b using the temporary value
        b = temp % b
    return a




# Choose e such that 1<e< phi(n) and e is coprime to phi(n)
def choose_e(phi):

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e



# Calculate d (private key exponent) using Extended Euclidan Algoritmh
# solving for d in d*e(mod(phi(n))) == 1
# logic from https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
def mod_inverse(e, phi):

    d = 0         # Will hold our private key value
    x_prev = 0    # coefficient 1
    x_curr = 1     # coefficient 2
    y_prev = 1       # coeficient 3
    temp_phi = phi   

    # algorithm
    while e > 0:

        # calculate quotient and remainder
        quotient = temp_phi // e
        remainder = temp_phi - quotient * e
        
        # swap values for next iteration
        temp_phi = e
        e = remainder

        # update values
        x_temp = x_curr - quotient * x_prev
        y_temp = d - quotient * y_prev

        # shift Values for next run through
        x_curr = x_prev
        x_prev = x_temp
        d = y_prev
        y_prev = y_temp

    # if gcd == 1, were all done
    if temp_phi == 1:
        return d + phi





# Encrypt the message using the public key(e, n)
def encrypt(message, e, n):
    ciphertext = []

    for char in message:
        m = ord(char)  # Convert character to ASCII
        c = pow(m, e, n)  # Encrypt using c ≡ m^e (mod n)
        ciphertext.append(c)

    return ciphertext





# Decrypt the ciphertext using the private key (d, n)
def decrypt(ciphertext, d, n):

    decrypted_message = []
    for char in ciphertext:
        m = pow(char, d, n)  # dcrypt using m ≡ c^d (mod n)
        decrypted_message.append(chr(m))  # convert ASCII to character

    return ''.join(decrypted_message)





# min function to execute the RSA algorithm
def rsa_algorithm():

    # set limit to 1000000
    p = generate_prime(1000000)  # gnerate prime numn p
    q = generate_prime(1000000)  # Generate prime num q
    n = p*q  # Calculate n = p * q
    phi = (p - 1) * (q - 1)  # Calculate phi(n)
    e = choose_e(phi)  # calc publiv exponent
    d = mod_inverse(e, phi)  # Calculate private exponent d


    # Print to mathc the assingment
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")


    message = input("enter message: ")
    ciphertext = encrypt(message, e, n)  # Encrypt message
    print(f"ciphertext: {ciphertext}")


    decrypted_message = decrypt(ciphertext, d, n)  # Decrypt message
    print(f"decrypted message: {decrypted_message}")





# run it
rsa_algorithm()

