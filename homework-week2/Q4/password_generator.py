import secrets
import string
import random

# Constant
pwd_length = 20
punc_length = 5

# Character set
alphabet_norm = string.ascii_letters + string.digits
alphabet_punc = string.punctuation

# Password part1 (letters & digits)
password_norm = ''.join(secrets.choice(alphabet_norm) for i in range(pwd_length - punc_length))

# Password part2 (punctuate)
password_punc = ''.join(secrets.choice(alphabet_punc) for j in range(punc_length))

# Generate position of punc characters
index_punc = random.sample(range(1, pwd_length), punc_length)
index_punc.sort()

# Generate position of norm characters
index_norm = []
for i in range(pwd_length):
    if i not in index_punc:
        index_norm.append(i)

# Initialization
password = [i for i in range(pwd_length)]

# Rearrange password characters
k = 0
for i in index_punc:
    password[i] = password_punc[k]
    k += 1

k = 0
for j in index_norm:
    password[j] = password_norm[k]
    k += 1

# Convert list to string
password_output = ''.join([str(e) for e in password])
# print(password)
print('Generated Password: ', password_output)
