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
specials = '~`! @#$%^&*()_-+={[}]|\:;\"\'<,>.?/'

char_count_condition_met = False
lower_condition_met = False
upper_condition_met = False
digit_condition_met = False
special_condition_met = False

no_of_chars = 12
chars = []
password = ''

for i in range(0, no_of_chars):
    # Generate combination of random characters from each character set.
    combo = [lowers[random.randint(0, len(lowers) - 1)],
             uppers[random.randint(0, len(uppers) - 1)],
             digits[random.randint(0, len(digits) - 1)],
             specials[random.randint(0, len(specials) - 1)]]

    # Randomly select character from combination.
    chars.append(combo[random.randint(0, len(combo) - 1)])


# Check validity.
# Check character count is sufficient.
if len(chars) >= no_of_chars:
    char_count_condition_met = True
else:
    char_count_condition_met = False    

# Check presence of lower case character.
for content in lowers:
    if content in chars:
        lower_condition_met = True
    else:
        pass

# Check presence of upper case character.
for content in uppers:
    if content in chars:
        upper_condition_met = True
    else:
        pass

# Check presence of digit character.
for content in digits:
    if content in chars:
        digit_condition_met = True
    else:
        pass

# Check presence of special character.
for content in specials:
    if content in chars:
        special_condition_met = True
    else:
        pass 


# Generate password from randomly select characters.
password = password.join(chars)

# If conditions met print password.
if char_count_condition_met == True and\
   lower_condition_met == True and\
   upper_condition_met == True and\
   digit_condition_met == True and\
   special_condition_met == True:
    print(password)
else:
    print("Password condition not met.")
