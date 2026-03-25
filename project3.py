import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits

all_chars = lower + upper + numbers

password_list = random.sample(all_chars, 8)

random.shuffle(password_list)

password = "".join(password_list)

print("Random Password:", password)