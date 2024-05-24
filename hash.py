
def hash_char_64(string):
    hash_value = 0
    for char in string:
        hash_value = (hash_value << 5) - hash_value + ord(char)
        hash_value &= 0xFFFFFFFFFFFFFFFF  # Masque sur 64 bits
    return hash_value