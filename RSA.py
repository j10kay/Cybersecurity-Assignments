import sympy, random, math

def compute_d(e, phi):
  if math.gcd(e, phi) != 1:
    print("e and phi must be coprime")
    return 0
  for d in range(3, phi, 2):
    result = (e*d) % phi
    if result == 1:
      return d

def RSA(prime_number_1, prime_number_2):
  message = random.randrange(1000)
  composite_number = prime_number_1 * prime_number_2
  phi = (prime_number_1 - 1) * (prime_number_2 - 1)
  e = sympy.randprime(3, phi)
  while phi % e == 0:
    e = sympy.randprime(3, phi)
  private_exponent = compute_d(e, phi)
  encrypted_message = (message**e) % composite_number
  decrypted_message = (encrypted_message ** private_exponent) % composite_number
  print("Alice hides everything except the values of n, {} and e, {}.\nn and e make up Alice's public key which she sends to Bob.\nBob encrypts his message (m), which in this case is {} by calculating m**e mod n.\n He gets an encrypted message (c), which evaluates to {} in this instance and sends this back to Alice.\nFinally, Alice decrypts his message using her private key, {} to perform the computation c ** d mod m.\nShe arrives at the message, {} which is identical to Bob's original message.\n".format(composite_number, e, message, encrypted_message, private_exponent, decrypted_message))
  return 

RSA(53, 59)
RSA(463, 499)
RSA(929, 983)
RSA(2011, 2017)
