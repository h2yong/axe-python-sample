"""transformers文本情感分析sample."""

import gradio as gr

from transformers import pipeline


classifier = pipeline("sentiment-analysis")


def analyze_sentiment(text):
    """简单transformers文本情感分析.

    :param text: 文本内容
    :returns
        情感分析结果
        执行度
    """
    result = classifier(text)[0]
    return f"情感: {result['label']}, 置信度: {result['score']:.2f}"


iface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")
iface.launch()
