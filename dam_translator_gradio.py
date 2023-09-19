import gradio as gr
from src import *


def encode_or_decode(str_input, radio):
    if radio == "人类语":
        return dam.string_to_charset(str_input)
    else:
        return dam.charset_to_string(str_input)
    

def hash_check(str_input, hash_input):
    hash_out = hash_confirmation.charset_to_shake256_charset(str_input)
    if hash_input == '':
        return hash_out, "未输入大坝哈希值"
    else:
        return hash_out, hash_confirmation.is_equal(hash_out, hash_input)


with gr.Blocks() as daba:
    with gr.Tab("翻译"):
        trans_inp = gr.Textbox(lines=5, label="输入")
        trans_rad = gr.Radio(["人类语", "大坝语"], label="选择输入的语言")
        trans_out = gr.Textbox(lines=5, label="输出")
        trans_button = gr.Button("TRANSLATE!")

    with gr.Tab("哈希校验"):
        hash_inp = gr.Textbox(lines=2, label="输入文本")
        hash_inp_hash = gr.Textbox(lines=5, label="输入大坝哈希值")
        hash_out = gr.Textbox(lines=5, label="大坝哈希值")
        hash_out_confirm = gr.Textbox(lines=1, label="校验结果")
        hash_button = gr.Button("校验")

    trans_button.click(encode_or_decode, inputs=[trans_inp, trans_rad], outputs=trans_out)
    hash_button.click(hash_check, inputs=[hash_inp, hash_inp_hash], outputs=[hash_out, hash_out_confirm])



if __name__ == "__main__":
    daba.launch(server_name="127.0.0.1", server_port=45454)

