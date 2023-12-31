import gradio as gr
from src import *


def encode_or_decode(str_input, radio):
    charset_list = {"大坝语": "dam", "尊嘟假嘟语": "zdjd", "emoji": "emoji"}
    try:
        out = dam.charset_to_string(str_input, charset_list[radio])
        return "参考译文：", out
    except:
        out = dam.string_to_charset(str_input, charset_list[radio])
        return f"监测到输入内容不是{radio}或输入有误，已自动翻译为{radio}：", out
    

def hash_check(str_input, hash_input):
    hash_out = hash_confirmation.charset_to_shake256_charset(str_input)
    if hash_input == '':
        return hash_out, "未输入大坝哈希值"
    else:
        return hash_out, hash_confirmation.is_equal(hash_out, hash_input)


with gr.Blocks() as daba:
    with gr.Tab("翻译"):
        trans_inp = gr.Textbox(lines=5, label="输入", placeholder="输入要翻译的内容")
        trans_rad = gr.Radio(["大坝语", "尊嘟假嘟语", "emoji"], label="选择翻译的语言", value="大坝语")
        trans_out_tag = gr.Textbox(lines=1, label="状态")
        trans_out = gr.Textbox(lines=5, label="输出")
        trans_button = gr.Button("TRANSLATE!")
        gr.Markdown(
            """
            # 大坝翻译器
            **!!! 此转换器仅为娱乐用途 !!!**
            
            项目源代码 <https://github.com/Loste1k/dam_translater>
            
            ## 如何使用
            在输入处填写文本，随后选择对应翻译语言，如果输入的为对应语言则会翻译成人类语，如果不是则会翻译成对应语言。
            """
        )

    with gr.Tab("哈希校验"):
        hash_inp = gr.Textbox(lines=2, label="输入文本")
        hash_inp_hash = gr.Textbox(lines=5, label="输入大坝哈希值")
        hash_out = gr.Textbox(lines=5, label="大坝哈希值")
        hash_out_confirm = gr.Textbox(lines=1, label="校验结果")
        hash_button = gr.Button("校验")


    trans_button.click(encode_or_decode, inputs=[trans_inp, trans_rad], outputs=[trans_out_tag, trans_out])
    hash_button.click(hash_check, inputs=[hash_inp, hash_inp_hash], outputs=[hash_out, hash_out_confirm])



if __name__ == "__main__":
    daba.launch(server_name="0.0.0.0", server_port=8080)
    # daba.launch(server_name="127.0.0.1", server_port=33333)

