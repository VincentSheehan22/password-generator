# Password Generator
#
# Script to generate a password.
#
# Password Rules:
#   1. Must contain min. of 8 characters.
#   2. Must include min. of 1 upper case characters.
#   3. Must include min. of 1 lower case characters.
#   4. Must include min. of 1 digit characters.
#   5. Must include min. of 1 special characters.


import random

lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = lowers.upper()
digits = '0123456789'
specials = '.\[{()*+?^$|'



password = f'{lowers[random.randint(0, len(lowers) - 1)]}' +\
           f'{uppers[random.randint(0, len(uppers) - 1)]}' +\
           f'{digits[random.randint(0, len(digits) - 1)]}' +\
           f'{specials[random.randint(0, len(specials) - 1)]}' +\
           f'{lowers[random.randint(0, len(lowers) - 1)]}' +\
           f'{uppers[random.randint(0, len(uppers) - 1)]}' +\
           f'{digits[random.randint(0, len(digits) - 1)]}' +\
           f'{specials[random.randint(0, len(specials) - 1)]}'

print(password)