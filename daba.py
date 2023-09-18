import base64
import hashlib
from random import randint


def get_shake256(input_string):
    sha_signature = hashlib.shake_256(input_string.encode()).hexdigest(5)
    return sha_signature


def encode_base64(input_str):
    input_bytes = input_str.encode("utf-8")
    encoded_bytes = base64.b64encode(input_bytes)
    return encoded_bytes.decode("utf-8")


def decode_base64(input_str):
    input_bytes = base64.b64decode(input_str)
    return input_bytes.decode("utf-8")


# 将字符串转换为base64编码
def convert_base64_to_charset(input_str, charset):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output_str = ""
    for char in input_str:
        # 获取字符在base64编码中的索引
        index = base64_chars.index(char)
        # 将索引转换为字符串
        output_str += charset[index % len(charset)]
    return output_str


# 将base64编码转换为字符串
def convert_charset_to_base64(input_str, charset):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output_str = ""
    for char in range(0, len(input_str), 3):
        # 获取字符在字符集中的索引
        index = charset.index(input_str[char] + input_str[char + 1] + input_str[char + 2])
        # 将索引转换为base64编码
        output_str += base64_chars[index % len(charset)]
    return output_str


def convert_shake256_to_charset(input_str):
    sha256_chars = "abcdef0123456789"
    output_str = "".join(charset[sha256_chars.index(char) % len(charset)] for char in input_str)
    return output_str


head = ['大', '打', '答', '沓', '哒', '耷', '嗒', '妲', '靼']
tail = ['把', '爸', '八', '拔', '罢', '粑', '坝', '疤']
charset = [h + t + ' ' for h in head for t in tail]


def main():
    try:
        equal, inequal = "相等", "不相等"
        human_lang_input = input("输入人类语：")
        encoded_str = encode_base64(human_lang_input)
        encoded_str_bc = convert_base64_to_charset(encoded_str, charset)
        sha256_str = get_shake256(human_lang_input)
        sha256_str_bc = convert_shake256_to_charset(sha256_str)
        print(f"大坝语为：{encoded_str_bc}\n大坝哈希为：{sha256_str_bc}")
        sha256_str_bc2 = input("输入大坝哈希值：").strip() + ' '
        print(f"大坝哈希值{equal if sha256_str_bc == sha256_str_bc2 else inequal}")

        daba_lang_input = input("输入大坝语：").strip() + ' '
        decoded_str_bc = convert_charset_to_base64(daba_lang_input, charset)
        decoded_str = decode_base64(decoded_str_bc)
        print("人类语为：", decoded_str)
    except Exception:
        excep_output = ['输入不规范，大坝两行泪', '你输你大坝啊，别输了', '我大坝你个大坝', '大坝你mua啊别大坝了',
                        '不会说大坝语去说zdjd语去']
        print(excep_output[randint(0, len(excep_output) - 1)])


if __name__ == "__main__":
    main()
