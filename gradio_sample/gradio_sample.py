"""Gradio sample."""

import gradio as gr
import numpy as np


def classify_image(image):
    """模拟一个图像分类模型.

    :param image: 图片
    :return 图片类型: 正方形图片/长方形图片
    """
    if image is None:
        return "请上传图片"
    # 这里我们只是简单判断图片是“正方形”还是“长方形”
    img_array = np.array(image)
    h, w, _ = img_array.shape
    if abs(h - w) < 20:  # 假设相差20像素以内算正方形
        return "正方形图片"
    return "长方形图片"


# 创建Gradio界面
iface = gr.Interface(
    fn=classify_image,  # 你的处理函数
    inputs=gr.Image(type="pil", label="上传图片"),  # 输入组件：图片上传
    outputs="text",  # 输出组件：文本
    title="简易图片分类器",
    description="上传一张图片，我来告诉你它是正方形还是长方形！",
)

iface.launch()  # 启动应用
