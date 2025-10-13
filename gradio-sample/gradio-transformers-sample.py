from transformers import pipeline
import gradio as gr

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    return f"情感: {result['label']}, 置信度: {result['score']:.2f}"

iface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")
iface.launch()