import random

def generateKey(prime_number, base):
  first_user_secret_number = random.randrange(100)
  first_user_message = (base ** first_user_secret_number) % prime_number
  second_user_secret_number = random.randrange(100)
  second_user_message = (base ** second_user_secret_number) % prime_number
  first_user_key = (second_user_message ** first_user_secret_number) % prime_number
  second_user_key = (first_user_message ** second_user_secret_number) % prime_number
  print("Alice and Bob agree on a prime number, {} and a base, {}.\nAlice chooses a secret number, {} and sends Bob {}.\nBob thinks of a secret number, {} and sends Alice {}.\nAlice performs some computations to obtain a secret key, {}.\nBob also performs similar computations to obtain a secret key, {}.\n".format(prime_number, base, first_user_secret_number, first_user_message, second_user_secret_number, second_user_message, first_user_key, second_user_key))
  return

generateKey(23, 5)
generateKey(67, 15)
generateKey(89, 33)
generateKey(97, 59)
