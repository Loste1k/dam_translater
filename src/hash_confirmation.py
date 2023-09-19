import hashlib
from . import dam

def get_shake256(input_str):
    sha_signature = hashlib.shake_256(input_str.encode()).hexdigest(5)
    return sha_signature


def shake256_to_charset(input_hash, charset):
    sha256_chars = "abcdef0123456789"
    output_str = "".join(charset[sha256_chars.index(char) % len(charset)] for char in input_hash)
    return output_str

def charset_to_shake256_charset(input_str):
    sha_inp = get_shake256(input_str)
    char_sha = shake256_to_charset(sha_inp, dam.set_charset())
    return char_sha

def is_equal(hash_1, hash_2):
    return "哈希相等" if hash_1.strip() == hash_2.strip() else "哈希不相等"
