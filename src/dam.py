import base64
import random

def set_charset(charset = 'dam'):
    if charset == "dam": return charset_dam()
    elif charset == "zdjd": return charset_zdjd()
    elif charset == "emoji": return charset_emoji()
    else: pass
    
    
def charset_dam():
    # 设置charset
    head = ['大', '打', '答', '沓', '哒', '耷', '嗒', '妲', '靼']
    tail = ['把', '爸', '八', '拔', '罢', '粑', '坝', '疤']
    table = []
    for i in range(len(head)):
        for j in range(len(tail)):
            table.append(head[i] + tail[j] + ' ')
    random.seed(1)
    random.shuffle(table)
    return table


def charset_zdjd():
    left = ['>', 'O', '^', 'o']
    mid = ['.', ',', 'v','_']
    right = ['<', 'o', '^', 'O']
    table = []
    for i in range(len(left)):
        for j in range(len(mid)):
            for k in range(len(right)):
                table.append('(' + left[i] + mid[j] + right[k] + ') ')
    random.seed(1)
    random.shuffle(table)
    return table


def charset_emoji():
    table = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣",
    "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰",
    "😘", "😗", "😙", "😚", "😋", "😛", "😜", "😝",
    "🤑", "🤗", "🤓", "😎", "🧐", "😏", "😒", "😞",
    "😔", "😟", "😕", "🙁", "🥵", "😣", "😖", "😫",
    "😩", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯",
    "😳", "🥺", "😨", "😰", "😥", "😓", "🤗", "🙄",
    "😪", "😴", "😷", "🤒", "🤕", "🤢", "🤮", "🤧",
    "🥴", "🤤", "🤠", "🥱", "😶", "😐", "😑", "😬"]
    return table


def string_to_base64(input_str):
    input_bytes = input_str.encode("utf-8")
    encoded_bytes = base64.b64encode(input_bytes)
    return encoded_bytes.decode("utf-8")


def base64_to_string(input_str):
    input_bytes = base64.b64decode(input_str)
    return input_bytes.decode("utf-8")


# 将字符串转换为base64编码
def base64_to_charset(input_str, charset):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output_str = ""
    for char in input_str:
        # 获取字符在base64编码中的索引
        index = base64_chars.index(char)
        # 将索引转换为字符串
        output_str += charset[index % len(charset)]
    return output_str


# 将base64编码转换为字符串
def charset_to_base64(input_str, charset):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output_str = ""
    char_len = len(charset[0])
    for char in range(0, len(input_str), char_len):
        # 获取字符在字符集中的索引
        index = charset.index(input_str[char:char+char_len])
        # 将索引转换为base64编码
        output_str += base64_chars[index % len(charset)]
    return output_str


def have_space_at_end(charset_name):
    return True if set_charset(charset_name)[0][-1] == ' ' else False


def string_to_charset(input_str, charset_name):
    # 将输入的人类语转换为base64格式
    encoded_str = string_to_base64(input_str)
    # 将base64格式转换为字符集
    encoded_str_bc = base64_to_charset(encoded_str, set_charset(charset_name))
    return encoded_str_bc


def charset_to_string(input_str_bc, charset_name):
    # try:
    space = ' ' if have_space_at_end(charset_name) else ''
    decoded_str_bc = charset_to_base64(input_str_bc.strip() + space, set_charset(charset_name))
    # 将base64格式转换为base64格式
    decoded_str = base64_to_string(decoded_str_bc)
    return decoded_str
    # except:
    #     # 如果出现异常，则提供异常信息
    #     excep_output = ['输入不规范，大坝两行泪',
    #                     '你输你大坝啊，别输了',
    #                     '我大坝你个大坝',
    #                     '大坝你mua啊别大坝了',
    #                     '不会说大坝语去说zdjd语去']
    #     return(excep_output[random.randint(0, len(excep_output) - 1)])


# def main():
#     try:
#         equal, inequal = "相等", "不相等"
#         human_lang_input = input("输入人类语：")
#         encoded_str = string_to_base64(human_lang_input)
#         encoded_str_bc = convert_base64_to_charset(encoded_str, charset)
#         sha256_str = get_shake256(human_lang_input)
#         sha256_str_bc = convert_shake256_to_charset(sha256_str)
#         print(f"大坝语为：{encoded_str_bc}\n大坝哈希为：{sha256_str_bc}")
#         sha256_str_bc2 = input("输入大坝哈希值：").strip() + ' '
#         print(f"大坝哈希值{equal if sha256_str_bc == sha256_str_bc2 else inequal}")

#         daba_lang_input = input("输入大坝语：").strip() + ' '
#         decoded_str_bc = convert_charset_to_base64(daba_lang_input, charset)
#         decoded_str = base64_to_string
#(decoded_str_bc)
#         print("人类语为：", decoded_str)
#     except:
#         excep_output = ['输入不规范，大坝两行泪', '你输你大坝啊，别输了', '我大坝你个大坝', '大坝你mua啊别大坝了',
#                         '不会说大坝语去说zdjd语去']
#         print(excep_output[random.randint(0, len(excep_output) - 1)])


# if __name__ == "__main__":
#     main()
