import random
import string
# Password generator
def generate_password(length):
    characters_pool = string.ascii_letters+string.digits+string.punctuation
    selected_characters = random.choices(characters_pool, k=length)
    password_string = ''.join(selected_characters)
    return password_string
password = generate_password(8)
print(f"Password generated successfully:{password}")