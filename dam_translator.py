import tkinter as tk
import base64
import random


def set_charset(seeds):
    # 设置charset
    head = ['大', '打', '答', '沓', '哒', '耷', '嗒', '妲', '靼']
    tail = ['把', '爸', '八', '拔', '罢', '粑', '坝', '疤']
    table = []
    for i in range(len(head)):
        for j in range(len(tail)):
            table.append(head[i] + tail[j] + ' ')
    random.seed(seeds)
    random.shuffle(table)
    return (table)


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
        index = charset.index(input_str[char] + input_str[char + 1] + input_str[char + 2])
        # 将索引转换为base64编码
        output_str += base64_chars[index % len(charset)]
    return output_str


def delete_output():
    output_box.delete(0.0, tk.END)


def human_2_daba():
    # 输入人类语
    input_str = entry.get()
    # 将输入的人类语转换为base64格式
    encoded_str = encode_base64(input_str)
    # 将base64格式转换为字符集
    encoded_str_bc = base64_to_charset(encoded_str, set_charset(1))
    # 打印转换后的大坝语
    delete_output()
    output_box.insert(tk.END, encoded_str_bc + "\n")


def daba_2_human():
    try:
        input_str_bc = entry.get().strip() + ' '
        # 将输入大坝语转换为字符集
        decoded_str_bc = charset_to_base64(input_str_bc, set_charset(1))
        # 将base64格式转换为base64格式
        decoded_str = decode_base64(decoded_str_bc)
        # 将base64格式转换为人类语
        delete_output()
        output_box.insert(tk.END, decoded_str + "\n")
    except:
        # 如果出现异常，则提供异常信息
        excep_output = ['输入不规范，大坝两行泪',
                        '你输你大坝啊，别输了',
                        '我大坝你个大坝',
                        '大坝你mua啊别大坝了',
                        '不会说大坝语去说zdjd语去']
        delete_output()
        output_box.insert(tk.END, excep_output[random.randint(0, len(excep_output) - 1)] + "\n")


def encode_or_decode():
    if var.get() == 'human2daba':
        human_2_daba()
    else:
        daba_2_human()


# 创建主窗口
root = tk.Tk()
root.geometry("400x300")
root.title("大坝语翻译器")

# 创建一个输入框
entry = tk.Entry(root)
entry.pack()
entry.focus()

# 创建一个radiobottom组
var = tk.StringVar()
radio_bottom = tk.Radiobutton(root, text="人类语 -> 大坝语", variable=var, value="human2daba", font=("Arial", 14))
radio_bottom.pack()
radio_bottom = tk.Radiobutton(root, text="大坝语 -> 人类语", variable=var, value="daba2human", font=("Arial", 14))
radio_bottom.pack()

# 创建一个按钮，用于调用print_text函数
button = tk.Button(root, text="-翻译-", command=encode_or_decode, font=("Arial", 14))
button.pack()

# 创建一个输出框
output_box = tk.Text(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 14))
output_box.config(width=60, height=20)
output_box.pack()

# 运行主循环
root.mainloop()
