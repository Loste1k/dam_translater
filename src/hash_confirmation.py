import hashlib


def get_shake256(input_string):
    sha_signature = hashlib.shake_256(input_string.encode()).hexdigest(5)
    return sha_signature


def shake256_to_charset(input_str, charset):
    sha256_chars = "abcdef0123456789"
    output_str = "".join(charset[sha256_chars.index(char) % len(charset)] for char in input_str)
    return output_str