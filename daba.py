import base64
from random import randint


def encode_base64(input_str):
   # 将字符串转换为utf-8编码
   input_bytes = input_str.encode("utf-8")
   # 将字节转换为base64编码
   encoded_bytes = base64.b64encode(input_bytes)
   # 将base64编码转换为字符串
   encoded_str = encoded_bytes.decode("utf-8")
   return encoded_str

def decode_base64(input_str):
   # 将base64编码解码为字节
   input_bytes = base64.b64decode(input_str)
   # 将字节转换为utf-8编码
   decoded_str = input_bytes.decode("utf-8")
   return decoded_str

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
 for char in range(0, len(input_str), 3):
     # 获取字符在字符集中的索引
     index = charset.index(input_str[char]+input_str[char+1]+input_str[char+2])
     # 将索引转换为base64编码
     output_str += base64_chars[index % len(charset)]
 return output_str


 # 设置charset
head = ['大','打','答','沓','哒','耷','嗒','妲','靼']
tail = ['把','爸','八','拔','罢','粑','坝','疤']
table = []
for i in range(len(head)):
    for j in range(len(tail)):
        table.append(head[i]+tail[j]+' ')
charset = table


try:
    # 输入人类语
    input_str = input("输入人类语：")

    # 将输入的人类语转换为base64格式
    encoded_str = encode_base64(input_str)
    # 将base64格式转换为字符集
    encoded_str_bc = base64_to_charset(encoded_str, charset)

    # 打印转换后的大坝语
    print("大坝语为：", encoded_str_bc)

    # 输入大坝语
    input_str_bc = input("输入大坝语：").strip()+' '
    # 将输入大坝语转换为字符集
    decoded_str_bc = charset_to_base64(input_str_bc, charset)
    # 将base64格式转换为base64格式
    decoded_str = decode_base64(decoded_str_bc)
    # 将base64格式转换为人类语
    print("人类语为：", decoded_str)
except Exception as e:
    # 如果出现异常，则提供异常信息
    excep_output = ['输入不规范，大坝两行泪',
                    '你输你大坝啊，别输了',
                    '我大坝你个大坝',
                    '大坝你mua啊别大坝了',
                    '不会说大坝语去说zdjd语去']
    print(excep_output[randint(0,len(excep_output)-1)])