import tkinter as tk
from src import *


def tk_input():
    return entry.get().strip()


def tk_output(str_output):
    delete_output()
    output_box.insert(tk.END, str_output + "\n")


def delete_output():
    output_box.delete(0.0, tk.END)


def encode_or_decode():
    str_input = tk_input()
    if var.get() == 'string2charset':
        tk_output(dam.string_to_charset(str_input))
    else:
        tk_output(dam.charset_to_string(str_input))


if __name__ == '__main__':
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
    radio_bottom = tk.Radiobutton(root, text="人类语 -> 大坝语", variable=var, value="string2charset", font=("Arial", 14))
    radio_bottom.pack()
    radio_bottom = tk.Radiobutton(root, text="大坝语 -> 人类语", variable=var, value="charset2string", font=("Arial", 14))
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